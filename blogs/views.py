from django.shortcuts import render
from . import models as blog_models

def index_view(request):
    queryset = blog_models.Blog.objects.all()[:10]

    return render(request, "blogs/index.html", {"blog_list": queryset})