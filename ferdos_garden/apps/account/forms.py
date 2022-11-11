from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User # for using django user table


class RegisterUser(forms.ModelForm):
    first_name=forms.CharField(label='نام',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control  shadow m-1','style':'border:0;font-size: 15px','PlaceHolder':'نام'}))
    last_name=forms.CharField(label='نام خانوادگی',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 15px;','PlaceHolder':'نام خانوادگی'}))
    username=forms.CharField(label='نام کاربری',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 15px;','PlaceHolder':'نام کاربری'}))
    email=forms.EmailField(label='ایمیل',error_messages={'required':'این فیلد نمی تواند خالی باشد','invalid':'ایمل ثبت شده معتبر نیست'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 15px;','PlaceHolder':'ایمیل'}))
    password1=forms.CharField(label='رمز',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.PasswordInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 15px;','PlaceHolder':'رمز'}))
    password2=forms.CharField(label='تکرار رمز',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.PasswordInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 15px;','PlaceHolder':'تکرار رمز'}))

    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']


    # validation first_name
    def clean_first_name(self):
        name=self.cleaned_data['first_name']
        if len(str(name)) <=2:
            raise forms.ValidationError('نام معتبر نیست')
        return name
    # validation last_name
    def clean_last_name(self):
        family=self.cleaned_data['last_name']
        if len(str(family)) ==1:
            raise forms.ValidationError('نام خانوادگی معتبر نیست')
        return family
    # validation password
    def clean_password2(self):
        password1=self.cleaned_data["password1"]
        password2=self.cleaned_data["password2"]
        if password1 and password2 and password1!=password2:
            raise forms.ValidationError('رمز ها یکسان نیست')
        else:
            password2
    # validation username
    def clean_username(self):
        user_name=self.cleaned_data['username']
        if len(user_name) <=5:
            raise forms.ValidationError('طول نام کاربری باید از ۵ حرف بیشتر باشد')
        else:
            return user_name





class LoginUser(forms.Form):
    username=forms.CharField(label='نام کاربری',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;','PlaceHolder':'username'}))
    password=forms.CharField(label='رمز عبور',error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.PasswordInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;','PlaceHolder':'password 1'}))

    def clean_username(self):
        user_name=self.cleaned_data['username']
        if len(str(user_name))<=5:
            raise forms.ValidationError('نام کاربری به درستی وارد نشده است')
        else:
            return user_name