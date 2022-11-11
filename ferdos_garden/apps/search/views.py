from django.shortcuts import render
from django.views import View
from django.db.models import Q
from apps.memory.models import Memory
from apps.blog. models import Blog
from django.shortcuts import render, redirect
# Create your views here.


class SearchResultsView(View):
    def get(self, request, *args, **kwargs) :
        query = self.request.GET.get("q")

        memories = Memory.objects.filter(Q(memory_title__icontains=query))
        blogs = Blog.objects.filter(Q(blog_title__icontains=query))
   
        context={
        "memories" :memories,
        "blogs": blogs
        }
        return render(request,'search_app/search_results.html',context)