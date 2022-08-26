from django.shortcuts import render

def show_blogs(request):
    return render(request,'blog_app/blogs_page.html')