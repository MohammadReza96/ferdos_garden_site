from django.shortcuts import render,redirect
from .forms import RegisterUser,LoginUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views import View


#----------------------------------------------------------------------------------------
class RegisterUserView(View):
    #use for show form,data 
    def get(self,request,*args,**kwargs):
        form=RegisterUser()
        return render(request,'registeruser/registeruser.html',{'form':form})
    
    #use for add data in table in database 
    def post(self,request,*args,**kwargs):
        form=RegisterUser(request.POST)
        if form.is_valid():
            data_cleaned=form.cleaned_data
            user=User(
                first_name=data_cleaned['first_name'],
                last_name=data_cleaned['last_name'],
                username=data_cleaned['username']
            )
            user.set_password(data_cleaned['password1'])  # for make a hash from password for using in database table
            user.save()
            messages.success(request,"کاربر گرامی ثبت نام شما با موفقیت انجام شد ، لطفا وارد شوید",'success')
            return redirect('account:login')
        else:
            return render(request,'registeruser/registeruser.html',{'form':form})   # return form with its errors
        
#----------------------------------------------------------------------------------------
class LoginUserView(View):
    
    def get(self,request,*args,**kwargs):
        form=LoginUser()
        return render(request,'loginuser/loginuser.html',{'form':form})
    
    def post(self,request,*args,**kwargs):
        form=LoginUser(request.POST)
        if form.is_valid():
            data_cleaned=form.cleaned_data
            user=authenticate(
                username=data_cleaned['username'],
                password=data_cleaned['password']
            )
            if user is not None:
                login(request,user)
                next_url=request.GET.get('next')  # save the page url
                print(next_url)
                if next_url is not None:
                    return redirect(next_url)
                return redirect('index:home')
            else:
                messages.warning(request,"کاربر ثبت شده موجود نیست",'warning')
                return render(request,'loginuser/loginuser.html',{'form':form})
        else:
            return render(request,'registeruser/registeruser.html',{'form':form})

#----------------------------------------------------------------------------------------
class LogoutUser(View):
    
    def dispatch(self, request,*args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('index:home')
        return super().dispatch(request,*args, **kwargs)
    
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('index:home')
    