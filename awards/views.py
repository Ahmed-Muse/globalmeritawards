from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import CommonAddCategoryForm,CommonAddCompanyForm,CommonAddVoteForm
from .models import CategoriesModel,CompaniesModel,VotesModel
from django.db import IntegrityError
from django.core.exceptions import ValidationError

from django.contrib import messages

def gmaWebsite(request):
    try:
        title="Global Merit Awards"
        context={"title":title,}
        return render(request,'awards/website/website.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def categories(request):
    try:
        title="Main Categories"
        allifqueryset=CategoriesModel.objects.all()
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/categories/categories.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def addCategory(request):
    try:
        title="Add New Category"
        form=CommonAddCategoryForm()
        if request.method == 'POST':
            form=CommonAddCategoryForm(request.POST or None)
            if form.is_valid():
                obj=form.save(commit=False)
                #obj.owner =user_var
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
def editCategory(request,pk):
    try:
        title="Update Category Details"
        update_allifquery=CategoriesModel.objects.get(id=pk)
        form =CommonAddCategoryForm(instance=update_allifquery)
        if request.method == 'POST':
            form =CommonAddCategoryForm(request.POST, instance=update_allifquery)
            if form.is_valid():
                obj=form.save(commit=False)
                #obj.owner =user_var
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

def deleteCategory(request,pk):
    try:
        CategoriesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:categories')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)


def companies(request):
    try:
        title="Main Categories"
        allifqueryset=CompaniesModel.objects.all()
        context = {
            "title":title,
            "allifqueryset":allifqueryset,
        }
        return render(request,'awards/companies/companies.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

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
def editCompany(request,pk):
    try:
        title="Update Company Details"
        update_allifquery=CompaniesModel.objects.get(id=pk)
        form =CommonAddCompanyForm(instance=update_allifquery)
        if request.method == 'POST':
            form =CommonAddCompanyForm(request.POST, instance=update_allifquery)
            if form.is_valid():
                obj=form.save(commit=False)
                #obj.owner =user_var
                obj.save()
                return redirect('awards:companies')
            else:
                form =CommonAddCompanyForm(instance=update_allifquery)
        else:
            form =CommonAddCompanyForm(instance=update_allifquery)
        context = {
            'form':form,
            "update_allifquery":update_allifquery,
            "title":title,
            
        }
        return render(request,'awards/companies/add-company.html',context)
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def deleteCompany(request,pk):
    try:
        CompaniesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:companies')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def addVote(request):
    #try:
        title="Add New Company"
        categories = CategoriesModel.objects.all()
        voted_categories = VotesModel.objects.filter(voter=request.user).values_list('category_id', flat=True)
        form=CommonAddVoteForm()
        forms = {}
        errors = {}
        for category in categories:
            if category.id not in voted_categories:
                if request.method == 'POST' and request.POST.get('category') == str(category.id):
                    form = CommonAddVoteForm(request.POST, category=category)
                    if form.is_valid():
                        try:
                            vote = form.save(commit=False)
                            vote.user = request.user
                            vote.category = category
                            vote.save()
                            return redirect('awards:vote')
                        except IntegrityError:
                            errors[category.name] = "You have already voted in this category."
                    else:
                        errors[category.name] = form.errors
                else:
                    form = CommonAddVoteForm()
                forms[category.name] = form

        #if request.method == 'POST':
            #form=CommonAddVoteForm(request.POST or None)
            #if form.is_valid():
                #obj=form.save(commit=False)
                #obj.owner =user_var
                #obj.save()
                #return redirect('awards:votes')
            #else:
                #form=CommonAddVoteForm()
        #else:
            #form=CommonAddVoteForm()
        context = {
            "title":title,
            "form":form,
            "voted_categories":voted_categories,
            
        }
        return render(request,'awards/votes/add-vote.html',context)
    
    #except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def voteForCompany(request,pk):
    try:
        title="Votes"
        allifquery=CompaniesModel.objects.get(id=pk)
        initial_votes=allifquery.votes
        allifquery.votes=initial_votes+1
        allifquery.save()

        return redirect('awards:companies')
    
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

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


    
def deleteVote(request,pk):
    try:
        VotesModel.objects.filter(id=pk).first().delete()
        return redirect('awards:votes')
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)  
    

def votecategory(request,pk):
    #category = get_object_or_404(CategoriesModel, id=pk)
    category=CategoriesModel.objects.filter(id=pk).first()
    if VotesModel.objects.filter(voter=request.user, category=category).exists():
        messages.error(request, "You have already voted in this category.")
        return redirect('awards:categories')
    print("before post")

    if request.method == 'POST':
        form = CommonAddVoteForm(request.POST)
        if form.is_valid():
            company_id=int(request.POST.get('company'))
            vote = form.save(commit=False)
            vote.user = request.user
            vote.category=category
            vote.save()
            cmpny=CompaniesModel.objects.filter(id=company_id).first()
            initial_votes=cmpny.votes
            cmpny.votes=initial_votes+1
            cmpny.save()

            messages.success(request, "Your vote has been recorded.")
            return redirect('awards:categories')
        else:
            print("not valid")
    else:
        print("after post")
        form = CommonAddVoteForm()
        form.fields['company'].queryset = CompaniesModel.objects.filter(category=category)

        context={
            'form': form, 'category': category

        }
    
    return render(request,'awards/votes/add-vote-category.html',context)

    return render(request, 'votes/vote.html', {'form': form, 'category': category})

@login_required
def vote_viewcopilot(request):
    categories = CategoriesModel.objects.all()
    if request.method == "POST":
        company_id = request.POST.get("company_id")
        try:
            company = CompaniesModel.objects.get(id=company_id)
            vote = VotesModel(voter=request.user, company=company)
            vote.save()
            return redirect("success")  # Redirect after successful vote
        except ValidationError as e:
            return render(request, "voting/vote.html", {"categories": categories, "error": str(e)})

    return render(request, "voting/vote.html", {"categories": categories})

@login_required
def vote(request):
    categories = CategoriesModel.objects.all()
    voted_categories = VotesModel.objects.filter(user=request.user).values_list('category_id', flat=True)
    forms = {}
    errors = {}

    for category in categories:
        if category.id not in voted_categories:
            if request.method == 'POST' and request.POST.get('category') == str(category.id):
                form =CommonAddVoteForm(request.POST, category=category)
                if form.is_valid():
                    try:
                        vote = form.save(commit=False)
                        vote.user = request.user
                        vote.category = category
                        vote.save()
                        return redirect('awards:vote')
                    except IntegrityError:
                        errors[category.name] = "You have already voted in this category."
                else:
                    errors[category.name] = form.errors
            else:
                form = CommonAddVoteForm(category=category)
            forms[category.name] = form
    return render(request, 'awards/vote.html', {'forms': forms, 'voted_categories': voted_categories, 'errors': errors})



from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def voting(request):
    categories = CategoriesModel.objects.all()
    if request.method == 'POST':
        for category in categories:
            company_id = request.POST.get(f'category_{category.id}')
            if company_id:
                company = get_object_or_404(CompaniesModel, id=company_id)
                vote, created = VotesModel.objects.get_or_create(
                    voter=request.user,
                    category=category,
                    defaults={'company': company},
                )
                if not created:
                    vote.company = company
                    vote.save()
        messages.success(request, "Your votes have been recorded!")
        return redirect('vote')

    return render(request, 'voting/vote.html', {'categories': categories})