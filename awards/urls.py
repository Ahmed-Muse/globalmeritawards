from django.urls import path
from . import views

app_name = 'awards'

urlpatterns = [
    path('', views.gmaWebsite, name="gmaWebsite"),
    path('Allifmaal/Admin/Home/CC/', views.allifAdminHome, name="allifAdminHome"),
    
    path('home/', views.home, name="home"),
    path('Categories/', views.categories, name="categories"),
    path('Category/Details/<int:pk>/', views.categoryDetails, name="categoryDetails"),
    
    path('Search/For/Categories/', views.categorySearch, name="categorySearch"),
    path('Add/New/Category/', views.addCategory, name="addCategory"),
    path('Edit/This/Category/<int:pk>/Update/Details/', views.editCategory, name="editCategory"),
    path('Delete/This/Category/<int:pk>/Permanently/', views.deleteCategory, name="deleteCategory"),

    path('Companies/', views.companies, name="companies"),
    path('Search/For/Companies/', views.companySearch, name="companySearch"),

    
    path('Add/New/Company/', views.addCompany, name="addCompany"),
    path('Edit/This/Company/<int:pk>/Update/Details/', views.editCompany, name="editCompany"),
    path('Delete/This/Company/<int:pk>/Permanently/4ever/', views.deleteCompany, name="deleteCompany"),
    path('Vote/For/This/Company/<int:pk>/U/Codey/', views.voteForCompany, name="voteForCompany"),
    path('Company/Details/<int:pk>/', views.companyDetails, name="companyDetails"),

    path('Votes/', views.votes, name="votes"),
    
    path('Delete/This/Vote/<int:pk>/Permanently/4ever/', views.deleteVote, name="deleteVote"),
    path('Vote/Details/<int:pk>/', views.voteDetails, name="voteDetails"),

    path('Vote/This/Cat/<int:pk>/', views.votecategory, name="votecategory"),


    path('gma/sponsors/', views.sponsors, name="sponsors"),
    path('gma/add/sponsor', views.addSponsor, name="addSponsor"),
    path('gma/edit/sponsor/details/<int:pk>/', views.editSponsor, name="editSponsor"),
    path('GMA/Sponsor/Details/<int:pk>/', views.sponsorDetails, name="sponsorDetails"),
    path('GMA/Delete/Sponsor/<int:pk>/', views.deleteSponsor, name="deleteSponsor"),

    path('gma/expenses/', views.expenses, name="expenses"),
    path('gma/add/expense', views.addExpense, name="addExpense"),
    path('gma/edit/expense/details/<int:pk>/', views.editExpense, name="editExpense"),
    path('GMA/Expense/Details/<int:pk>/', views.expenseDetails, name="expenseDetails"),
    path('GMA/Delete/Expense/<int:pk>/', views.deleteExpense, name="deleteExpense"),
    
]