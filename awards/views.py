from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CommonAddCategoryForm,CommonAddCompanyForm,CommonAddVoteForm,AddExpenseForm,AddSponsorForm
from .models import CategoriesModel,CompaniesModel,VotesModel,SponsorsModel,ExpensesModel
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from loginapp.decorators import allifmaal_admin_supperuser,logged_in_user_is_owner_ceo,logged_in_user_can_add,logged_in_user_can_view,logged_in_user_can_edit,logged_in_user_can_delete,logged_in_user_is_admin
from django.contrib import messages
from django.db.models import Q
from loginapp.models import User

def gmaWebsite(request):
    try:
        title="Global Merit Awards"
        context={"title":title,}
        return render(request,'awards/website/website.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@allifmaal_admin_supperuser
def allifAdminHome(request):
    try:
        logged_user=request.user
        categories=CategoriesModel.objects.all().order_by('-votes')[:2]
        catcount=CategoriesModel.objects.all().count()
        companies=CompaniesModel.objects.all().order_by('-votes')[:2]
        compcount=CompaniesModel.objects.all().count()
        sponsors=SponsorsModel.objects.all().order_by('-amount')[:2]
        expenses=ExpensesModel.objects.all().order_by('-amount')[:2]
        allifqueryset=User.objects.all().order_by('-castedvotes')[:2]
        voterscount=User.objects.all().count()
        votes=VotesModel.objects.all().order_by('-date')[:2]
        votescount=VotesModel.objects.all().count()
        expensescount=ExpensesModel.objects.all().count()
        sponsorscount=SponsorsModel.objects.all().count()
        
        title="Allifmaal Admin"
        context={"title":title,"logged_user":logged_user,"allifqueryset":allifqueryset,
                 "categories":categories,"companies":companies,"votes":votes,"expenses":expenses,
                 "sponsors":sponsors,"catcount":catcount,"compcount":compcount,"voterscount":voterscount,
                 "votescount":votescount,"expensescount":expensescount,"sponsorscount":sponsorscount,}
        return render(request,'awards/home/allif-admin-home.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo    
def home(request):
    try:
        logged_user=request.user
        categories=CategoriesModel.objects.all().order_by('-votes')[:2]
        catcount=CategoriesModel.objects.all().count()
        companies=CompaniesModel.objects.all().order_by('-votes')[:2]
        compcount=CompaniesModel.objects.all().count()
        sponsors=SponsorsModel.objects.all().order_by('-amount')[:2]
        expenses=ExpensesModel.objects.all().order_by('-amount')[:2]
        allifqueryset=User.objects.all().order_by('-castedvotes')[:2]
        voterscount=User.objects.all().count()
        votes=VotesModel.objects.all().order_by('-date')[:2]
        votescount=VotesModel.objects.all().count()
        expensescount=ExpensesModel.objects.all().count()
        sponsorscount=SponsorsModel.objects.all().count()
        
        title="Global Merit Awards"
        context={"title":title,"logged_user":logged_user,"allifqueryset":allifqueryset,
                 "categories":categories,"companies":companies,"votes":votes,"expenses":expenses,
                 "sponsors":sponsors,"catcount":catcount,"compcount":compcount,"voterscount":voterscount,
                 "votescount":votescount,"expensescount":expensescount,"sponsorscount":sponsorscount,}
        return render(request,'awards/home/home.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def categories(request):
    try:
        title="Categories"
        allifqueryset=CategoriesModel.objects.all()
        logged_user=request.user
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
            "logged_user":logged_user,
        }
        return render(request,'awards/categories/categories.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def categoryDetails(request,pk):
    try:
        title="Category Details"
        logged_user=request.user
        allifquery=CategoriesModel.objects.filter(id=pk).first()
        allifqueryset=CompaniesModel.objects.filter(category=allifquery)
        companies_counter=CompaniesModel.objects.filter(category=allifquery).count()
        cat_voters=allifquery.voter.all()
        cat_voters_counter=allifquery.voter.all().count()
        user_voting_status=''
        user_is_admin_owner=False
        if logged_user in cat_voters:
            user_voting_status="You already voted for this category"
        else:
            user_voting_status="You are yet to vote for this category"
        if logged_user.user_category=="owner" or logged_user.user_category=="admin":
            user_is_admin_owner=True
        else:
            user_is_admin_owner=False

        context = {
            "title":title,
            "allifquery":allifquery,
            "allifqueryset":allifqueryset,
            "logged_user":logged_user,
            "cat_voters":cat_voters,
            "cat_voters_counter":cat_voters_counter,
            "companies_counter":companies_counter,
            "user_voting_status":user_voting_status,
            "user_is_admin_owner":user_is_admin_owner,
        }
        return render(request,'awards/categories/category-details.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def categorySearch(request):
    try:
        title="Search"
        if request.method=='POST':
            allifsearch=request.POST.get('allifsearchcommonfieldname')
            searched_data=CategoriesModel.objects.filter((Q(name__icontains=allifsearch)))
            context={
            "title":title,
            "allifsearch":allifsearch,
            "searched_data":searched_data,
        }
        return render(request,'awards/categories/categories.html',context)
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def addCategory(request):
    try:
        title="Add New Category"
        form=CommonAddCategoryForm()
        if request.method == 'POST':
            form=CommonAddCategoryForm(request.POST or None)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                return redirect('awards:categories')
            else:
                form=CommonAddCategoryForm()
        else:
            form=CommonAddCategoryForm()
        context = {
            "title":title,
            "form":form,
        }
        return render(request,'awards/categories/add-category.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def editCategory(request,pk):
    try:
        title="Update Category Details"
        update_allifquery=CategoriesModel.objects.get(id=pk)
        form =CommonAddCategoryForm(instance=update_allifquery)
        if request.method == 'POST':
            form =CommonAddCategoryForm(request.POST, instance=update_allifquery)
            if form.is_valid():
                obj=form.save(commit=False)
                obj.save()
                return redirect('awards:categories')
            else:
                form =CommonAddCategoryForm(instance=update_allifquery)
        else:
            form =CommonAddCategoryForm(instance=update_allifquery)
        context = {
            'form':form,
            "update_allifquery":update_allifquery,
            "title":title,
            
        }
        return render(request,'awards/categories/add-category.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
@logged_in_user_can_delete
def deleteCategory(request,pk):
    try:
        CategoriesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:categories')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def companies(request):
    try:
        title="Companies"
        logged_user=request.user
        allifqueryset=CompaniesModel.objects.all()
        user_is_admin_owner=False
        if logged_user.user_category=="owner" or logged_user.user_category=="admin":
            user_is_admin_owner=True
        else:
            user_is_admin_owner=False

        context = {
            "title":title,
            "allifqueryset":allifqueryset,
            "logged_user":logged_user,
            "user_is_admin_owner":user_is_admin_owner,
            
        }
        return render(request,'awards/companies/companies.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
def companySearch(request):
    try:
        title="Search"
        if request.method=='POST':
            allifsearch=request.POST.get('allifsearchcommonfieldname')
            searched_data=CompaniesModel.objects.filter((Q(name__icontains=allifsearch)|Q(category__name__icontains=allifsearch)))
            context={
            "title":title,
            "allifsearch":allifsearch,
            "searched_data":searched_data,
        }
        return render(request,'awards/companies/companies.html',context)
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'loginapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def addCompany(request):
    try:
        title="Add New Company"
        form=CommonAddCompanyForm()
        if request.method == 'POST':
            form=CommonAddCompanyForm(request.POST or None)
            if form.is_valid():
                obj=form.save(commit=False)
                #obj.owner =user_var
                obj.save()
                return redirect('awards:companies')
            else:
                form=CommonAddCompanyForm()
        else:
            form=CommonAddCompanyForm()
        context = {
            "title":title,
            "form":form,
            
        }
        return render(request,'awards/companies/add-company.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'allifmaalcommonapp/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def editCompany(request,pk):
    try:
        title="Update Company Details"
        allifquery=CompaniesModel.objects.get(id=pk)
        form =CommonAddCompanyForm(instance=allifquery)
        if request.method == 'POST':
            form =CommonAddCompanyForm(request.POST, instance=allifquery)
            if form.is_valid():
                obj=form.save(commit=False)
                #obj.owner =user_var
                obj.save()
                return redirect('awards:companies')
            else:
                form =CommonAddCompanyForm(instance=allifquery)
        else:
            form =CommonAddCompanyForm(instance=allifquery)
        context = {
            'form':form,
            "allifquery":allifquery,
            "title":title,
            
        }
        return render(request,'awards/companies/add-company.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def companyDetails(request,pk):
    try:
        title="Company Details"
        allifquery=CompaniesModel.objects.filter(id=pk).first()
        allifqueryset=allifquery.voter.all()
       
        context = {
            "title":title,
            "allifquery":allifquery,
            "allifquery":allifquery,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/companies/company-details.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def deleteCompany(request,pk):
    try:
        CompaniesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:companies')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)


############### VOTES ####################
@login_required(login_url='loginapp:userLoginPage')
def votes(request):
    try:
        title="Votes"
        allifqueryset=VotesModel.objects.all()
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/votes/votes.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    

@login_required(login_url='loginapp:userLoginPage')
def voteForCompany(request,pk):
    try:
        logged_user=request.user
        user=User.objects.filter(email=request.user.email).first()
       
        allifquery=CompaniesModel.objects.filter(id=pk).first()
        if VotesModel.objects.filter(voter=request.user,category=allifquery.category).exists():
            messages.error(request, "You already voted in this Category. ")
            return redirect('awards:companies')
        else:
            try:
                VotesModel.objects.create(company=allifquery,voter=logged_user,category=allifquery.category)
                allifquery.votes += 1
                
                category=CategoriesModel.objects.filter(id=allifquery.category.id).first()
                category.votes += 1
                allifquery.save()
                category.save()
                user.castedvotes+=1
                user.save()
                
                messages.success(request, "You voted successfully.")
                return redirect('awards:companies')
            except Exception as e:
                messages.error(request, f"Error: {e}")
                return redirect('awards:companies')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo    
def deleteVote(request,pk):
    try:
        VotesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:votes')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)  
    

def votecategory(request,pk):
    title="Vote Here"
    category=CategoriesModel.objects.filter(id=pk).first()
    user=User.objects.filter(email=request.user.email).first()
    if VotesModel.objects.filter(voter=request.user, category=category).exists():
        messages.error(request, "You already voted in this Category. ")
        return redirect('awards:categories')
    print("before post")
    if request.method == 'POST':
        form = CommonAddVoteForm(request.POST)
        if form.is_valid():
            company_id = form.cleaned_data['company'].id # get company id from cleaned data
            vote = form.save(commit=False)
            vote.voter = request.user  # changed user to voter to match your model.
            vote.category = category
            company_obj = CompaniesModel.objects.filter(id=company_id).first()
            if company_obj:
                company_obj.voter.add(request.user)
                category.voter.add(request.user)
                company_obj.save()
                category.votes += 1
                company_obj.votes +=1
                user.castedvotes+=1
                category.save()
                company_obj.save()
                vote.company = company_obj # add company to vote object
                vote.save()
                user.save()

                messages.success(request, "Your vote has been recorded.")
                return redirect('awards:categories')
            else:
                messages.error(request, "Invalid company selected.")
                return redirect('awards:categories')
        else:
            print("form is not valid")
            form.fields['company'].queryset = CompaniesModel.objects.filter(category=category) #re-add the queryset.
            context = {
                'form': form,
                'category': category,
                "title": title,
            }
            return render(request, 'awards/votes/add-vote-category.html', context)
    else:
        print("after post")
        form = CommonAddVoteForm()
        form.fields['company'].queryset = CompaniesModel.objects.filter(category=category)

    context = {
        'form': form,
        'category': category,
        "title": title,
    }

    return render(request, 'awards/votes/add-vote-category.html', context)

@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def voteDetails(request,pk):
    try:
        title="Vote Details"
        allifquery=VotesModel.objects.filter(id=pk).first()
        context = {
            "title":title,
            "allifquery":allifquery,
            "allifquery":allifquery,
        }
        return render(request,'awards/votes/vote-details.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)


##############################33 suppliers section ###############3
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def sponsors(request):
    try:
        title="Sponsors"
        allifqueryset=SponsorsModel.objects.all()
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/sponsors/sponsors.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def addSponsor(request):
    try:
        title="Add New Sponsor"
        form=AddSponsorForm()
        if request.method=='POST':
            form=AddSponsorForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('awards:sponsors')
            else:
                form=AddSponsorForm()
        else:
            form=AddSponsorForm()
        context = {
            "title":title,
            "form":form,
        }
        return render(request,'awards/sponsors/add-sponsor.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def editSponsor(request,pk):
    try:
        title="Update Sponsor Details"
        user_var_update=SponsorsModel.objects.filter(id=pk).first()
        form=AddSponsorForm(instance=user_var_update)
        if request.method=='POST':
            form=AddSponsorForm(request.POST or None, instance=user_var_update)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('awards:sponsors')
            else:
                form=AddSponsorForm(instance=user_var_update)
        else:
            form=AddSponsorForm(instance=user_var_update)
           
        context={"title":title,"form":form,}
        return render(request,'awards/sponsors/add-sponsor.html',context)
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def sponsorDetails(request,pk):
    try:
        title="Sponsor Details"
        allifquery=SponsorsModel.objects.filter(id=pk).first()
        context={
            "allifquery":allifquery,
            "title":title,
        }
        return render(request,'awards/sponsors/sponsor-details.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def deleteSponsor(request,pk):
    try:
        SponsorsModel.objects.filter(id=pk).first().delete()
        return redirect('awards:sponsors')
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

##################33 expenses ####################3
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def expenses(request):
    try:
        title="Expenses"
        allifqueryset=ExpensesModel.objects.all()
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/expenses/expenses.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def addExpense(request):
    try:
        title="Add New Expense"
        form=AddExpenseForm()
        if request.method=='POST':
            form=AddExpenseForm(request.POST)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('awards:expenses')
            else:
                form=AddExpenseForm()
        else:
            form=AddExpenseForm()
        context = {
            "title":title,
            "form":form,
        }
        return render(request,'awards/expenses/add-expense.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def editExpense(request,pk):
    try:
        title="Update Expense Details"
        user_var_update=ExpensesModel.objects.filter(id=pk).first()
        form=AddExpenseForm(instance=user_var_update)
        if request.method=='POST':
            form=AddExpenseForm(request.POST or None, instance=user_var_update)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.save()
                return redirect('awards:expenses')
            else:
                form=AddExpenseForm(instance=user_var_update)
        else:
            form=AddExpenseForm(instance=user_var_update)
           
        context={"title":title,"form":form,}
        return render(request,'awards/expenses/add-expense.html',context)
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
    
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def expenseDetails(request,pk):
    try:
        title="Expense Details"
        allifquery=ExpensesModel.objects.filter(id=pk).first()
        context={
            "allifquery":allifquery,
            "title":title,
        }
        return render(request,'awards/expenses/expense-details.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
@login_required(login_url='loginapp:userLoginPage')
@logged_in_user_is_owner_ceo
def deleteExpense(request,pk):
    try:
        ExpensesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:expenses')
       
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)
