from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateNewCustomUserForm,CustomUserLoginForm,UpdateCustomUserForm
from django.contrib.auth import authenticate, login, logout#for login and logout- and authentication
from loginapp.models import User
from django.contrib.auth.decorators import login_required
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
                username=request.POST.get('username')
                password=request.POST.get('password')
                user=authenticate(request,username=username,password=password)
                if user !=None:
                    if user.is_superuser==True:# this is very important..only allifmaal team allowed to be superusers
                        user_var="username"#arbitary parameters values
                        usrslg="allifmaal2116e7b104a5d8e7kkjfsjh6rewr#fdskjengltd"
                        if user is not None:#if there is an authenticated user
                            login(request, user)
                            return redirect('awards:categories')
                        else:
                            messages.info(request,'Sorry! your email or password is incorrect!')
                            form=CustomUserLoginForm()
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
            return redirect('allifmaalusersapp:userLoginPage')
        else:
            return redirect('allifmaalusersapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)


def editUserDetailsByAdmin(request,allifslug):
    try:
        if request.user.is_authenticated:
            user=User.objects.filter(customurlslug=allifslug).first()
            title="Update User Details"
            form=UpdateCustomUserForm(instance=user)
            if request.method=='POST':
                form=UpdateCustomUserForm(request.POST or None, instance=user)
                if form.is_valid():
                    form.save()
                    return redirect('allifmaalcommonapp:CommonDecisionPoint')
            context={"title":title,"form":form,}
            return render(request,"allifmaalusersapp/users/edit_user.html",context)
        else:
            return redirect('allifmaalusersapp:userLoginPage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)
   
def changeYourUserPassword(request):
    try:
        title="Change Your User Password"
        if request.user.is_authenticated:
            logged_user=request.user
            if request.method=='POST':
                pass1=request.POST.get('password1')
                pass2=request.POST.get('password2')
                if pass2==pass1:
                    user=User.objects.filter(email=logged_user.email).first()
                    user.set_password(str(pass1))
                    user.save()
                    logout(request)
                    return redirect('allifmaalusersapp:userLoginPage')
                else:
                    messages.info(request,'Sorry the two passwords are not the same')
                    return redirect('allifmaalusersapp:changeYourUserPassword')
                    
            context={"title":title,"logged_user":logged_user,}
            return render(request,"allifmaalusersapp/users/changeyourpasswrd.html",context)
        else:
            return redirect('allifmaalusersapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)

def changeUserPasswordByAdmin(request,allifslug):
    try:
        user=User.objects.filter(customurlslug=allifslug).first()
        title="Change User Password"
        if request.user.is_authenticated:
            if request.method=='POST':
                pass1=request.POST.get('password1')
                pass2=request.POST.get('password2')
                if pass2==pass1:
                    user=User.objects.filter(email=user.email).first()
                    user.set_password(str(pass1))
                    user.save()
                    return redirect('allifmaalcommonapp:CommonDecisionPoint')
                else:
                    messages.info(request,'Sorry the two passwords are not the same')
                    return redirect('allifmaalusersapp:changeUserPasswordByAdmin',allifslug=user.customurlslug)
                    
            context={"title":title,"user":user,}
            return render(request,"allifmaalusersapp/users/changeuserpassbyadmin.html",context)
        else:
            return redirect('allifmaalusersapp:userLoginPage')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)

def changeUserToSupperuserByAdmin(request,allifslug):
    try:
        if request.user.is_authenticated:
            user=User.objects.filter(customurlslug=allifslug).first()
            if user.is_staff==True and user.is_superuser==True:
                user.is_staff=False
                user.is_superuser=False
                user.is_active=True
            else:
                user.is_staff=True
                user.is_superuser=True
                user.is_active=True
            user.save()
            return redirect('allifmaalcommonapp:CommonDecisionPoint')
        else:
            return redirect('allifmaalcommonapp:CommonDecisionPoint')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)
#customurlslug customuserslug
def DeleteUserByAdmin(request,allifslug):
    try:
        if request.user.is_authenticated:
            User.objects.filter(customurlslug=allifslug).first().delete()
            return redirect('allifmaalcommonapp:CommonDecisionPoint')
        else:
            return redirect('allifmaalusersapp:userLoginPage')
        
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)

def userForgotPassowrd(request):#this requires the user to remember their email and secret key
    try:
        title="Change Your Password"
        if request.method=='POST':
            accessemail=request.POST.get('email')
            secretkey=request.POST.get('secretkey')
            pass1=request.POST.get('password1')
            pass2=request.POST.get('password2')
            usremail=User.objects.filter(email=accessemail,customurlslug=secretkey).first()
            if usremail is not None:
                if pass2==pass1:
                    usremail.set_password(str(pass1))
                    usremail.save()
                    messages.success(request, 'Your password was successfully changed!')
                    return redirect('allifmaalusersapp:userForgotPassowrd')
                else:
                    messages.info(request,'Sorry the two passwords are not the same')
                    return redirect('allifmaalusersapp:userForgotPassowrd')
            else:
                messages.info(request,'Your email or secret key is incorrect!')
                return redirect('allifmaalusersapp:userForgotPassowrd')
            
        return render(request,"allifmaalusersapp/users/userforgotpass.html",{"title":title,})
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalusersapp/error/error.html',error_context)






@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanAdd(request,pk,*allifargs,**allifkwargs):
    try:
        allifquery=User.objects.filter(id=pk).first()
        user_var=request.user.usercompany
        usrslg=request.user.customurlslug
        if allifquery.can_add==True:
            allifquery.can_add=False
        else:
            allifquery.can_add=True
        allifquery.can_do_all=False
        allifquery.save()
        return redirect('allifmaalcommonapp:commonUserDetails',pk=allifquery.id,allifusr=usrslg,allifslug=user_var)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalcommonapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanView(request,pk,*allifargs,**allifkwargs):
    try:
        allifquery=User.objects.filter(id=pk).first()
        user_var=request.user.usercompany
        usrslg=request.user.customurlslug
        if allifquery.can_view==True:
            allifquery.can_view=False
        else:
            allifquery.can_view=True
        allifquery.can_do_all=False
        allifquery.save()
        return redirect('allifmaalcommonapp:commonUserDetails',pk=allifquery.id,allifusr=usrslg,allifslug=user_var)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalcommonapp/error/error.html',error_context)
@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanEdit(request,pk,*allifargs,**allifkwargs):
    try:
        allifquery=User.objects.filter(id=pk).first()
        user_var=request.user.usercompany
        usrslg=request.user.customurlslug
        if allifquery.can_edit==True:
            allifquery.can_edit=False
        else:
            allifquery.can_edit=True
        allifquery.can_do_all=False
        allifquery.save()
        return redirect('allifmaalcommonapp:commonUserDetails',pk=allifquery.id,allifusr=usrslg,allifslug=user_var)
   
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalcommonapp/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage') 
def commonUserCanDelete(request,pk,*allifargs,**allifkwargs):
    try:
        allifquery=User.objects.filter(id=pk).first()
        user_var=request.user.usercompany
        usrslg=request.user.customurlslug
        if allifquery.can_delete==True:
            allifquery.can_delete=False
        else:
            allifquery.can_delete=True
        allifquery.can_do_all=False 
        allifquery.save()
        return redirect('allifmaalcommonapp:commonUserDetails',pk=allifquery.id,allifusr=usrslg,allifslug=user_var)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalcommonapp/error/error.html',error_context)