# from django.shortcuts import render, redirect 
# from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django import forms
from django import forms

class SignUpForm(UserCreationForm): 
        def __init__(self, *args, **kwargs): 
            super().__init__(*args, **kwargs) 
            self.fields['username'].widget.attrs.update({ 
            'class': 'form-control form-control-md', 
            'required':'', 
            'name':'cutsname', 
            'id':'username', 
            'type':'text', 
            'placeholder':'John Doe', 
            'maxlength': '16', 
            'minlength': '6', 
            }) 
        
        class Meta: 
            model = User 
            fields = ['username']

    

#     def __init__(self, *args, **kwargs): 
#         super().__init__(*args, **kwargs) 
#         self.fields['fristname'].widget.attrs.update({ 
#             'class': 'form-control form-control-md', 
#             'required':'', 
#             'name':'cutsname', 
#             'id':'fristname', 
#             'type':'text', 
#             'placeholder':'enter name', 
#             'maxlength': '16', 
#             'minlength': '6', 
#             }) 
 
 
#     fristname = forms.CharField(max_length=20, label=False) 

 
