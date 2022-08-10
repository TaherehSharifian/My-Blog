from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import ListView

from . import models
from . import forms
# Create your views here.


class StartView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date']

    def get_queryset(self):
        queryset = super().get_queryset()[:3]
        return queryset


class AllPostsView(ListView):
    model = models.Post
    template_name = 'blog/all-posts.html'
    context_object_name = 'posts'


class PostDetailView(View):

    def get(self, req, slug):
        post = models.Post.objects.get(slug=slug)
        tags = post.tags.all()
        comment_form = forms.CommentForm()
        comments = post.comments.all().order_by('-id')
        context = {'post': post, 'tags': tags,
                   'comment_form': comment_form, 'comments': comments}
        return render(req, 'blog/post-detail.html', context)

    def post(self, req, slug):
        post = models.Post.objects.get(slug=slug)
        comment_form = forms.CommentForm(req.POST)

        if comment_form.is_valid():
            cm_form = comment_form.save(commit=False)
            cm_form.post = post
            cm_form.save()
            return redirect('post-detail', slug)

        tags = post.tags.all()
        context = {'post': post, 'tags': tags, 'comment_form': comment_form}
        return render(req, 'blog/post-detail.html', context)



# def starting_page(request):
#     post_list = models.Post.objects.all().order_by('-date')[:3]
#     context = {'posts': post_list}
#     return render(request, 'blog/index.html', )

# def posts(request):
#     post_list = models.Post.objects.all()
#     context = {'posts': post_list}
#     return render(request, 'blog/all-posts.html', context)

# def post_detail(request, slug):
#     post = get_object_or_404(models.Post, slug=slug)
#     context = {'post':post, 'tags': post.tags.all()}
#     return render(request, 'blog/post-detail.html', context)

