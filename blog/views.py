from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.urls import reverse
import logging
from blog.models import Post
from django.core.paginator import Paginator
from .forms import ContactForm

# posts=[
#     {'id':1,'title':'Post 1', 'content': "Content of Post 1"},
#     {'id':2,'title':'Post 2', 'content': "Content of Post 2"},
#     {'id':3,'title':'Post 3', 'content': "Content of Post 3"},
#     {'id':4,'title':'Post 4', 'content': "Content of Post 4"},
# ]

def index(request):
    # Getting data from Post model
    all_posts=Post.objects.all()
    paginator=Paginator(all_posts,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)

    blog_title='Latest Posts'
    return render(request, 'blog/index.html',{'blog_title':blog_title,'page_obj':page_obj})

def detail(request,slug):
    # Below line is for getting static data
    # post=next((item for item in posts if item['id'] == post_id), None)
    # logger=logging.getLogger('TESTING')
    # logger.debug(f'post value is {post}')
    try:
        post= Post.objects.get(slug=slug)
        related_posts=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Blog Post Doesn't exist")

    return render(request, 'blog/detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse("blog:new"))

def new_url_view(request):
    return HttpResponse("This is the redirected new page")

def contact(request):
    if (request.method=='POST'):
        form = ContactForm(request.POST)
        logger=logging.getLogger('TESTING')
        if form.is_valid():
            logger.debug(f'post data of contact form is {form.cleaned_data['name']},{form.cleaned_data['email']},{form.cleaned_data['message']}')
        else:
            logger.debug(f'Form validation Failed')
    return render(request, 'blog/contact.html')