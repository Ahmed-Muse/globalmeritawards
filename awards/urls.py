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
    path('Add/New/Votes/', views.addVote, name="addVote"),
    path('Delete/This/Vote/<int:pk>/Permanently/4ever/', views.deleteVote, name="deleteVote"),

    path('Vote/This/Cat/<int:pk>/', views.votecategory, name="votecategory"),

    

    path('vote/', views.vote, name='vote'),
]