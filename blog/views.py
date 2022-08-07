from django.shortcuts import render, get_object_or_404

from . import models
# Create your views here.

# 

def starting_page(request):
    post_list = models.Post.objects.all().order_by('-date')[:3]
    context = {'posts': post_list}
    return render(request, 'blog/index.html', context)

def posts(request):
    post_list = models.Post.objects.all()
    context = {'posts': post_list}
    return render(request, 'blog/all-posts.html', context)

def post_detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    context = {'post':post, 'tags': post.tags.all()}
    return render(request, 'blog/post-detail.html', context)

