from django.shortcuts import render,redirect
from apps.form.models import Message
from apps.form.form import Message_Form
from django.contrib import messages

def show_form(request):
    form=Message_Form(request.POST)
    if form.is_valid():
        clean_data=form.cleaned_data
        final_form=Message()
        final_form.first_name=clean_data['first_name']
        final_form.last_name=clean_data['last_name']
        final_form.email=clean_data['email']
        final_form.title=clean_data['title']
        final_form.text=clean_data['text']
        final_form.save()
        messages.success(request,'فرم شما با موفقیت ارسال شد','success')
        return redirect('index:home')
    else:
        context={'form':form}
        return render(request,'form/form.html',context)
