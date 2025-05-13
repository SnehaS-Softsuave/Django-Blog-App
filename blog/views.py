from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from blog.models import Post

# posts=[
#     {'id':1,'title':'Post 1', 'content': "Content of Post 1"},
#     {'id':2,'title':'Post 2', 'content': "Content of Post 2"},
#     {'id':3,'title':'Post 3', 'content': "Content of Post 3"},
#     {'id':4,'title':'Post 4', 'content': "Content of Post 4"},
# ]

def index(request):
    # Getting data from Post model
    posts=Post.objects.all()
    blog_title='Latest Posts'
    return render(request, 'blog/index.html',{'blog_title':blog_title,'posts':posts})

def detail(request,slug):
    # Below line is for getting static data
    # post=next((item for item in posts if item['id'] == post_id), None)
    # logger=logging.getLogger('TESTING')
    # logger.debug(f'post value is {post}')
    try:
        post= Post.objects.get(slug=slug)
    except Post.DoesNotExist:
        raise Http404("Blog Post Doesn't exist")

    return render(request, 'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new"))

def new_url_view(request):
    return HttpResponse("This is the redirected new page")