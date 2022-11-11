from django import forms
from django.core import validators

#------------------------------------------------------------------------------------------ contact form class
CHOICES = [('انتقاد', 'انتقاد'), ('پیشنهاد', 'پیشنهاد'),('سایر', 'سایر')]

class ContactForm(forms.Form):
    name = forms.CharField(label='نام',label_suffix=" ",error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;','PlaceHolder':'سارا'}))
    family = forms.CharField(label='فامیل',label_suffix=" ",error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'میرزایی'}))
    choice_title = forms.CharField(label='عنوان پیام',label_suffix=" ",widget=forms.Select(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;margin:10px'},choices=CHOICES),initial='پیشنهاد')
    email = forms.EmailField(label='ایمیل',label_suffix=" ",error_messages={'required':'این فیلد نمی تواند خالی باشد','invalid':'ایمل ثبت شده معتبر نیست'},widget=forms.TextInput(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'ایمیل'}))
    message = forms.CharField(label='پیام',label_suffix=" ",error_messages={'required':'این فیلد نمی تواند خالی باشد'},widget=forms.Textarea(attrs={'class':'form-control shadow m-1','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'متن پیام'}))



    # validation parts
    def clean_name(self):
        name=self.cleaned_data['name']
        if len(str(name)) <=2:
            raise forms.ValidationError('نام معتبر نیست')
        return name
    
    def clean_family(self):
        family=self.cleaned_data['family']
        if len(str(family)) ==1:
            raise forms.ValidationError('نام خانوادگی معتبر نیست')
        return family
    
    
    # def clean_email(self):                 # this validatore check the email if exit in server 
    #     email=self.cleaned_data['email']
    #     is_valid = validate_email(str(email),verify=True)
    #     if is_valid == None:
    #         raise forms.ValidationError('! ایمیل وجود خارجی ندارد')
    #     return email
    
    


# class ContactForm_us(forms.ModelForm):       # show form using class class view
#     class Meta:
#         model=ContactModel_us
#         fields=('name','family','title','email','phone','message')
#         widgets={
#             'name':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px;','PlaceHolder':'سارا'}),
#             'family':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'میرزایی'}),
#             'title':forms.Select(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px'},choices=CHOICES),
#             'email':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'ایمیل'}),
#             'phone':forms.TextInput(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'شماره تماس'}),
#             'message':forms.Textarea(attrs={'class':'form-control shadow','style':'border:0;font-size: 20px;margin:10px','PlaceHolder':'متن پیام'})
#         }






# print(validate_email('mohammad.r.yazdaniyan@gmail.com',verify=True))
