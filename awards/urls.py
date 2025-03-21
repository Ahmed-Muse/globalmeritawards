from django.urls import path
from . import views

app_name = 'awards'

urlpatterns = [
    path('', views.gmaWebsite, name="gmaWebsite"),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('vote/', views.vote, name='vote'),
]