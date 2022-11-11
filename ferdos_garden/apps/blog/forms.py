from django import forms
from .models import BlogIdea


class BlogIdeaForm(forms.ModelForm):

            
    class Meta:
        model=BlogIdea
        fields=('full_name','email','blog_idea')
        widgets={
             'full_name':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px;','PlaceHolder':'سارا'}),
             'email':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'ایمیل'}),
             'blog_idea':forms.Textarea(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'متن پیام'})
         }