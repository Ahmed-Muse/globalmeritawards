from django import forms
from loginapp.models import User
from .models import CategoriesModel,CompaniesModel,VotesModel

class CommonAddCategoryForm(forms.ModelForm):
    class Meta:
        model = CategoriesModel
        fields = ['name','comments']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'comments':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
        }

class CommonAddCompanyForm(forms.ModelForm):
    class Meta:
        model = CompaniesModel
        fields = ['name','category','comments','votes']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'comments':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
             'votes':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'category':forms.Select(attrs={'class':'form-control','placeholder':''}),
        }
class CommonAddVoteForm(forms.ModelForm):
   
    class Meta:
        model = VotesModel
        fields = ['voter','company','category']
        widgets={
            'voter':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'company':forms.Select(attrs={'class':'form-control','placeholder':''}),
           
        }

