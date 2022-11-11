from django import forms
from .models import Memory,MemoryGallary


#---------------------------------------------------------------------------------------
class MemoryForm(forms.ModelForm):
    memory_title=forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control  shadow m-1 my-2','style':'border:0;font-size: 15px','PlaceHolder':'عنوان خاطره'}))
    memory_text=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control  shadow m-1','style':'border:0;font-size: 15px','PlaceHolder':'متن خاطره'}))
    class Meta:
        model=Memory
        fields=['memory_title','memory_text']

#---------------------------------------------------------------------------------------
class MemoryGallaryForm(forms.ModelForm):
    memory_image=forms.FileField(label="",widget=forms.FileInput(attrs={'class':'form-control  shadow my-2','style':'border:0;font-size: 15px'}))
    class Meta:
        model=MemoryGallary
        fields=['memory_image']
