from django.db import models
from loginapp.models import User
from django.db import models
from django import forms
class CategoriesModel(models.Model):
    name= models.CharField(max_length=30,blank=False,null=True)
    comments= models.CharField(null=True, blank=True, max_length=30)
    date=models.DateField(blank=True,null=True,auto_now_add=True)
   
    def __str__(self):
        return str(self.name)

class CompaniesModel(models.Model):
    name= models.CharField(max_length=100,blank=False,null=True)
    category = models.ForeignKey(CategoriesModel, on_delete=models.SET_NULL, related_name='categores',null=True,blank=True)
    comments= models.CharField(null=True, blank=True, max_length=30)
    date=models.DateField(blank=True,null=True,auto_now_add=True)
    votes=models.DecimalField(max_digits=10,blank=True,null=True,decimal_places=1,default=0)
    def __str__(self):
        return str(self.name)

class VotesModel(models.Model):
    voter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='votes',null=True)
    company = models.ForeignKey(CompaniesModel, on_delete=models.SET_NULL,null=True)
   
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(CategoriesModel, on_delete=models.SET_NULL, related_name='categoriesvotes',null=True,blank=True)
    class Meta:
        unique_together = ('voter', 'category')  # Enforce one vote per catego
    def __str__(self):
        return f"{self.voter.username} voted for {self.company.name} in {self.voter.username}"
    
