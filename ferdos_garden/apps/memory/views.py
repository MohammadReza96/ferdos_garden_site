from django.shortcuts import render,redirect
from django.views import View
from .models import Memory,MemoryGallary,MemoryLike
from .forms import MemoryForm,MemoryGallaryForm
from django.forms import modelformset_factory
from django.http import HttpResponse,HttpResponseNotFound
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

#-----------------------------------------------------------------------------------------------------------------------------
class ShowMemory(View):
    def get(self,request,*args,**kwargs):
        memories=Memory.objects.filter(memory_is_active=True)
        pagenator=Paginator(memories,4)
        page_number=request.GET.get('page')
        page_object=pagenator.get_page(page_number)
        if request.user.is_authenticated:
            list_memory_like=MemoryLike.objects.filter(user_like=request.user.id).values('memory_id')
            list_memory_like_id=[memory['memory_id']  for memory in list_memory_like]
            return render(request,'memories/memories.html',{'page_obj':page_object,'list_memory_like_id':list_memory_like_id})
        
        
        return render(request,'memories/memories.html',{'page_obj':page_object})

#-----------------------------------------------------------------------------------------------------------------------------
@login_required
def add_memory(request):
    image_FormSet=modelformset_factory(MemoryGallary,form=MemoryGallaryForm,extra=4)

    if request.method=="GET":
        memory_form=MemoryForm()
        image_formset=image_FormSet(queryset=MemoryGallary.objects.none())
        context={
                    'memory_form':memory_form,
                    'image_formset':image_formset
                }
        return render(request,'addmemory/addmemory.html',context)
    
    #----------------------------------------------------------------------------------
    elif request.method=="POST":
        memory_form=MemoryForm(request.POST)
        image_formset=image_FormSet(request.POST,request.FILES)
        
        if memory_form.is_valid() and image_formset.is_valid():
            data=memory_form.cleaned_data
            memory=Memory.objects.create(
                memory_title=data['memory_title'],
                memory_text=data['memory_text'],
                user_register=request.user
            )
            for form in image_formset.cleaned_data:
                if form:
                    MemoryGallary.objects.create(
                        memory_image=form['memory_image'],
                        memory=memory
                    )
            messages.success(request,'خاطره با موفقیت ثبت شد','success')
            return redirect('memory:_memory')
        else:
            context={
                        'memory_form':memory_form,
                        'image_formset':image_formset
                    }
            messages.error(request,'خاطره با موفقیت ثبت نشد','danger')
            return render(request,'addmemory/addmemory.html',context)

#----------------------------------------------------------------------------------------------------------------------------- function type for like
# def like(request):
#     if request.method=='GET':
#         memory_id=request.GET['memory_id']
#         memory=Memory.objects.get(id=memory_id)
#         likememory=MemoryLike.objects.filter(memory__id=memory.id,user_like=request.user.id)
#         if not likememory:
#             likememory=MemoryLike(memory=memory)
#             likememory.user_like=request.user
#             likememory.save()
#         return HttpResponse('Success')
#     return HttpResponse('UnSuccess')


#----------------------------------------------------------------------------------------------------------------------------- class type for like
class like(View):
    def get(self,request,*args,**kwargs):
        memory_id=request.GET['memory_id']
        memory=Memory.objects.get(id=memory_id)
        likememory=MemoryLike.objects.filter(memory__id=memory.id,user_like=request.user.id)
        if not likememory:
            likememory=MemoryLike(memory=memory)
            likememory.user_like=request.user
            likememory.save()
            return HttpResponse('Success')
        return HttpResponse('UnSuccess')
    
    

