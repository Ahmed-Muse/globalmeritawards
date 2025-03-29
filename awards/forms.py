from django import forms
from loginapp.models import User
from .models import CategoriesModel,CompaniesModel,VotesModel


############################# start of datepicker customization ##############################
class DatePickerInput(forms.DateInput):#use this class whereever you have a date and it will give you the calender
    input_type = 'date'#
class TimePickerInput(forms.TimeInput):#use this wherever you have time input
    input_type = 'time'
class DateTimePickerInput(forms.DateTimeInput):#use this wherever you have datetime input
    input_type = 'datetime'
    ################################# end of datepicker customization ################################

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
        fields = ['name','category','comments','votes','voter','add_date']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'comments':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
             'votes':forms.TextInput(attrs={'class':'form-control','placeholder':''}),
            'category':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'add_date' : DatePickerInput(attrs={'class':'form-control'}),
        }
class CommonAddVoteForm(forms.ModelForm):
   
    class Meta:
        model = VotesModel
        fields = ['voter','company','category','reasons']
        widgets={
            'voter':forms.Select(attrs={'class':'form-control','placeholder':''}),
            'company':forms.Select(attrs={'class':'form-control custom-field-class-for-seclect2','placeholder':''}),
            'reasons':forms.Textarea(attrs={'class':'form-control','placeholder':''}),
            'category':forms.Select(attrs={'class':'form-control custom-field-class-for-seclect2','placeholder':''}),
           
        }

