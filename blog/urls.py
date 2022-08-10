from django.urls import path

from . import views

urlpatterns = [
    path('', views.StartView.as_view(), name='starting-page'),
    path('posts', views.AllPostsView.as_view(), name='posts'),
    path('posts/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
]