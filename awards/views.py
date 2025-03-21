from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, VoteForm
from .models import Category, Vote

def gmaWebsite(request):
    try:
        title="Global Merit Awards"
        context={"title":title,}
        return render(request,'awards/website/website.html',context)
    except Exception as ex:
        error_context={'error_message': ex,}
        return render(request,'awards/error/error.html',error_context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('awards:vote')
    else:
        form = RegistrationForm()
    return render(request, 'awards/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('awards:vote')
    else:
        form = AuthenticationForm()
    return render(request, 'awards/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('awards:login')
from django.db import IntegrityError
@login_required
def vote(request):
    categories = Category.objects.all()
    voted_categories = Vote.objects.filter(user=request.user).values_list('category_id', flat=True)
    forms = {}
    errors = {}

    for category in categories:
        if category.id not in voted_categories:
            if request.method == 'POST' and request.POST.get('category') == str(category.id):
                form = VoteForm(request.POST, category=category)
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
                form = VoteForm(category=category)
            forms[category.name] = form
    return render(request, 'awards/vote.html', {'forms': forms, 'voted_categories': voted_categories, 'errors': errors})


from .models import Category, Company, Vote
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def voting(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        for category in categories:
            company_id = request.POST.get(f'category_{category.id}')
            if company_id:
                company = get_object_or_404(Company, id=company_id)
                vote, created = Vote.objects.get_or_create(
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