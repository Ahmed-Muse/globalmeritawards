from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('awards/', include('awards.urls')),
    path('loginapp/', include('loginapp.urls')),
]