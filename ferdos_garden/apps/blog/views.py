from django.shortcuts import render
from .models import Blog,BlogGallary,Tag
from django.core.paginator import Paginator
from .models import BlogIdea
from .forms import BlogIdeaForm
from django.contrib import messages


#-------------------------------------------------
def show_blogs(request):
    blogs=Blog.objects.filter(blog_status=True)
    pagenator=Paginator(blogs,4)
    page_number=request.GET.get('page')
    page_object=pagenator.get_page(page_number)
    return render(request,'blogs/blogs.html',{'page_obj':page_object})

#-------------------------------------------------
def show_blog(request,blog_slug):
    blog=Blog.objects.get(blog_slug=blog_slug)
    blog_tag=Tag.objects.filter(blog__blog_slug=blog_slug)
    blog_gallery=BlogGallary.objects.filter(blog__blog_slug=blog_slug)
    blog_idea=BlogIdea.objects.filter(blog_slug=blog_slug)
    blog.blog_view_number=blog.blog_view_number+1
    form=BlogIdeaForm()
    blog.save()
    
    context={
        'blog':blog,
        'blog_tag':blog_tag,
        'blog_gallery':blog_gallery,
        'blog_idea':blog_idea,
        'form':form
    }
    
    if request.method=='POST':
        form_1=BlogIdeaForm(request.POST)
        if form_1.is_valid():
            new_form=form_1.cleaned_data
            final_form=BlogIdea()
            final_form.blog_slug=blog_slug
            final_form.full_name=new_form['full_name']
            final_form.email=new_form['email']
            final_form.blog_idea=new_form['blog_idea']
            blog.blog_view_number=blog.blog_view_number-1
            final_form.save()
            blog.save()
            return render(request,'blog/blog.html',context)
        else:
            blog.blog_view_number=blog.blog_view_number-1
            blog.save()
            context['form']=form_1
            return render(request,'blog/blog.html',context)
    else:
        return render(request,'blog/blog.html',context)
