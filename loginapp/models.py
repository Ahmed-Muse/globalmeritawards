from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify
from uuid import uuid4

class User(AbstractUser):# this is for creating new user... the fields are below and those from parent class
    user_level= [
    ('owner','owner'),
    ('chairman','chairman'),
    ('ceo','ceo'),
    ('director','director'),
    ('genmanager','genmanager'),
    ('admin','admin'),
    ('staff', 'staff'),
    ('guest', 'guest'),
    ]
    #db_table = 'auth_user'# you may uncomment this if you get cusotmization related errors and see if will solve
    USERNAME_FIELD = 'email'
    username = models.CharField(max_length=255, null=True,blank=True)
    email = models.EmailField(('email address'), unique=True) # changes email to unique and blank to false
    first_name= models.CharField(max_length=255, null=True,blank=False)
    last_name= models.CharField(max_length=255, null=True,blank=False)
    REQUIRED_FIELDS = ['username','first_name','last_name'] # removes email from REQUIRED_FIELDS
    user_category= models.CharField(choices=user_level, default='guest', max_length=100,null=True,blank=True)
    fullNames= models.CharField(max_length=255, null=True,blank=True,default="User Full Names")
    phone=models.CharField(max_length=50,blank=True,null=True)
    can_do_all=models.BooleanField('Can do all',default=False)
    can_add=models.BooleanField('Can add',default=False)
    can_edit=models.BooleanField('Can edit',default=False)
    can_view=models.BooleanField('Can view',default=False)
    can_delete=models.BooleanField('Can delete',default=False)
    date=models.DateField(blank=True,null=True,auto_now_add=True)
    castedvotes=models.IntegerField(blank=True,null=True,default=0)
    can_access_all=models.BooleanField('Can access all',default=False)
    can_access_related=models.BooleanField('Can access only related',default=False)
    allifmaal_admin=models.BooleanField('Can access all',default=False)
   
    def __str__(self):
        return str(self.first_name)#please dont change this unless very necessary....
    
class UserLoginDetailsModel(models.Model):#this is for the login
    username = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255, null=True)
   
    def __str__(self):
        return self.username
