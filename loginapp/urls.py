from django.urls import path
from . import views
app_name='loginapp'
urlpatterns = [
path('New/User/Registration/Create/Page/', views.newUserRegistration, name="newUserRegistration"),
path('User/Login/Page/', views.userLoginPage, name="userLoginPage"),
path('User/Logout/Page/', views.userLogoutPage, name="userLogoutPage"),
path('Users/', views.users, name="users"),
path('Search/For/Users/', views.userSearch, name="userSearch"),
path('User/Details/<int:pk>/', views.userDetails, name="userDetails"),
path('Edit/User/Details/<int:pk>/Update/', views.editUserDetailsByAdmin, name="editUserDetailsByAdmin"),
path('Delete/This/User/<int:pk>/', views.DeleteUserByAdmin, name="DeleteUserByAdmin"),
path('Change/Your/User/Password/Page/', views.changeYourUserPassword, name="changeYourUserPassword"),
path('User/Admin/Change/User/Password/New/Password/Page/<int:pk>/', views.changeUserPasswordByAdmin, name="changeUserPasswordByAdmin"),

##############################33  controls #################
path('User/Can/Add/Only/<int:pk>/', views.commonUserCanAdd, name="commonUserCanAdd"),
path('User/Can/View/Only/<int:pk>/', views.commonUserCanView, name="commonUserCanView"),
path('User/Can/Edit/Only/<int:pk>/', views.commonUserCanEdit, name="commonUserCanEdit"),
path('User/Can/Delete/Only/<int:pk>/', views.commonUserCanDelete, name="commonUserCanDelete"),





]   
