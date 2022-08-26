from django import forms

class Message_Form(forms.Form):
    first_name=forms.CharField(max_length=15,label='نام',initial='سارا')
    last_name=forms.CharField(max_length=20,label='نام خانوادگی',initial='جعفری')
    email=forms.EmailField(label='ایمیل',initial='sara_jafary@gmail.com')
    title=forms.CharField(max_length=30,label='عنوان پیام')
    text=forms.CharField(label='پیام',initial='متن مورد نظر',widget=forms.Textarea)