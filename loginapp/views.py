from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateNewCustomUserForm,CustomUserLoginForm,UpdateCustomUserForm
from django.contrib.auth import authenticate, login, logout#for login and logout- and authentication
from loginapp.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .decorators import allifmaal_admin_supperuser,logged_in_user_is_owner_ceo,logged_in_user_can_add,logged_in_user_can_view,logged_in_user_can_edit,logged_in_user_can_delete,logged_in_user_is_admin
# Create your views here.
def newUserRegistration(request):
    try:
        title="New User Registeration"
        if request.user.is_authenticated:
            return redirect("loginapp:userLoginPage")
        else:
            form=CreateNewCustomUserForm()
            if request.method=='POST':
                form=CreateNewCustomUserForm(request.POST)
                email=request.POST.get('email')
                fname=request.POST.get('first_name')
                lname=request.POST.get('last_name')
                if form.is_valid():
                    obj = form.save(commit=False)
                    obj.fullNames=str(f'{fname}+{lname}')#important...used to generate user slug
                    obj.save()
                    return redirect("loginapp:userLoginPage")
                else:
                    messages.info(request,f'Sorry {email} is likely taken, or passwords not match')
        context={"title":title,"form":form,}
        return render(request,"loginapp/users/user_registeration.html",context)
    except Exception as ex:
        error_context={'error_message': ex,"title": title,}
        return render(request,'loginapp/error/error.html',error_context)

def userLoginPage(request):
    try:
        title="User Login Page"
        if request.user.is_authenticated:
            return redirect("awards:categories")
        else:
            form=CustomUserLoginForm()#nthis form is not used...normally html form is used instead in this case.
            if request.method=='POST':
                form=CustomUserLoginForm(request.POST)
                if form.is_valid():
                    username=request.POST.get('username')
                    password=request.POST.get('password')
                    user=authenticate(request,username=username,password=password)
                    if user !=None:
                        if user.is_superuser==True:# this is very important..only allifmaal team allowed to be superusers
                            
                            if user is not None:#if there is an authenticated user
                                login(request, user)
                                return redirect('awards:allifAdminHome')
                            else:
                                messages.info(request,'Sorry! your email or password is incorrect!')
                                form=CustomUserLoginForm()
                        elif user.user_category=="owner":
                            login(request, user)
                            return redirect('awards:home')
                        
                        else:
                            if user is not None:#if there is an authenticated user
                                login(request, user)
                                return redirect('awards:categories')
                            else:
                                messages.info(request,'Sorry! your email or password is incorrect!')
                                form=CustomUserLoginForm()
                    else:
                        messages.info(request,'Sorry! your email or password is incorrect!')
                        form=CustomUserLoginForm()
                else:
                    messages.info(request,'Sorry! your inputs are incorrect!')
                    form=CustomUserLoginForm()
            else:
                form=CustomUserLoginForm()
                
        context={"form":form,"title":title,}
        return render(request,"loginapp/users/user_login.html",context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
        
def userLogoutPage(request):
    try:
        if request.user.is_authenticated:
            logout(request)#logs user out
            messages.success(request,"Successfully logged out ")
            return redirect('loginapp:userLoginPage')
        else:
            return redirect('loginapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def users(request):
    try:
        allifqueryset=User.objects.all()
        title="Registered Users"
        
        context={"title":title,
                "allifqueryset":allifqueryset,
                }
        return render(request,"loginapp/users/users.html",context)
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')   
def editUserDetailsByAdmin(request,pk):
    try:
        if request.user.is_authenticated:
            user=User.objects.filter(id=pk).first()
            title="Update User Details"
            form=UpdateCustomUserForm(instance=user)
            if request.method=='POST':
                form=UpdateCustomUserForm(request.POST or None, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('loginapp:users')
            context={"title":title,"form":form,}
            return render(request,"loginapp/users/edit_user.html",context)
        else:
            return redirect('loginapp:userLoginPage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
   
@login_required(login_url='loginapp:userLoginPage') 
def changeYourUserPassword(request):
    try:
        title="Change Your User Password"
        if request.user.is_authenticated:
            logged_user=request.user
            user_email=logged_user.email
            if request.method=='POST':
                pass1=request.POST.get('password1')
                pass2=request.POST.get('password2')
                if pass2==pass1:
                    user=User.objects.filter(email=logged_user.email).first()
                    user.set_password(str(pass1))
                    user.save()
                    logout(request)
                    return redirect('loginapp:userLoginPage')
                else:
                    messages.info(request,'Sorry the two passwords are not the same')
                    return redirect('loginapp:changeYourUserPassword')
                    
            context={"title":title,"logged_user":logged_user,"user_name":user_email,}
            return render(request,"loginapp/users/changeyourpasswrd.html",context)
        else:
            return redirect('loginapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage') 
def changeUserPasswordByAdmin(request,pk):
    try:
        user=User.objects.filter(id=pk).first()
        title="Change User Password"
        if request.user.is_authenticated:
            if request.method=='POST':
                pass1=request.POST.get('password1')
                pass2=request.POST.get('password2')
                if pass2==pass1:
                    user=User.objects.filter(email=user.email).first()
                    user.set_password(str(pass1))
                    user.save()
                    return redirect('loginapp:users')
                else:
                    messages.info(request,'Sorry the two passwords are not the same')
                    return redirect('loginapp:changeUserPasswordByAdmin',pk=user.id)
                    
            context={"title":title,"user":user,}
            return render(request,"loginapp/users/changeuserpassbyadmin.html",context)
        else:
            return redirect('loginapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def DeleteUserByAdmin(request,pk):
    try:
        if request.user.is_authenticated:
            User.objects.filter(id=pk).first().delete()
            return redirect('loginapp:users')
        else:
            return redirect('loginapp:userLoginPage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def userSearch(request):
    try:
        title="Search"
        if request.method=='POST':
            allifsearch=request.POST.get('allifsearchcommonfieldname')
            searched_data=User.objects.filter((Q(first_name__icontains=allifsearch)|Q(last_name__icontains=allifsearch)))
            context={
            "title":title,
            "allifsearch":allifsearch,
            "searched_data":searched_data,
        }
        return render(request,"loginapp/users/users.html",context)
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
def userDetails(request,pk):
    try:
        if request.user.is_authenticated:
            allifquery=User.objects.filter(id=pk).first()
            title="User Details"
            canadd=allifquery.can_add
            canview=allifquery.can_view
            canedit=allifquery.can_edit
            candelete=allifquery.can_delete
            context={"title":title,
                    "allifquery":allifquery,
                    "allifquery":allifquery,
                    "canadd":canadd,
                    "canview":canview,
                    "canedit":canedit,
                    "candelete":candelete,}
            return render(request,"loginapp/users/user-details.html",context)
        else:
            return redirect('loginapp:userLoginPage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanAdd(request,pk):
    try:
        allifquery=User.objects.filter(id=pk).first()
        if allifquery.can_add==True:
            allifquery.can_add=False
        else:
            allifquery.can_add=True
        allifquery.can_do_all=False
        allifquery.save()
        print(allifquery.can_add)
        return redirect('loginapp:userDetails',pk=allifquery.id)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanView(request,pk):
    try:
        allifquery=User.objects.filter(id=pk).first()
        if allifquery.can_view==True:
            allifquery.can_view=False
        else:
            allifquery.can_view=True
        allifquery.can_do_all=False
        allifquery.save()
        return redirect('loginapp:userDetails',pk=allifquery.id)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanEdit(request,pk):
    try:
        allifquery=User.objects.filter(id=pk).first()
        if allifquery.can_edit==True:
            allifquery.can_edit=False
        else:
            allifquery.can_edit=True
        allifquery.can_do_all=False
        allifquery.save()
        return redirect('loginapp:userDetails',pk=allifquery.id)
   
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanDelete(request,pk):
    try:
        allifquery=User.objects.filter(id=pk).first()
        if allifquery.can_delete==True:
            allifquery.can_delete=False
        else:
            allifquery.can_delete=True
        allifquery.can_do_all=False 
        allifquery.save()
        return redirect('loginapp:userDetails',pk=allifquery.id)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)