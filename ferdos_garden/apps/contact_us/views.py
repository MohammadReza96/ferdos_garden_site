from django.shortcuts import render
from .models import ContactModel
from .forms import ContactForm
from django.contrib import messages
from django.http import JsonResponse



def contact_us(request):
    form=ContactForm()
    if request.method=='POST':
        form_1=ContactForm(request.POST)
        if form_1.is_valid():
            data=form_1.cleaned_data
            finall_form=ContactModel()
            finall_form.name=data['name']
            finall_form.family=data['family']
            finall_form.title=data['choice_title']
            finall_form.email=data['email']
            finall_form.message=data['message']
            finall_form.save()
            messages.success(request,'پیام شما با موفقیت ارسال شد','success')
            return render(request,'contact_us/contact_us.html',{'form':form})
        else:
            messages.error(request,'لطفا فیلد ها را اصلاح کنید','danger')
            return render(request,'contact_us/contact_us.html',{'form':form_1})
    else:
        return render(request,'contact_us/contact_us.html',{'form':form,'flag':3})