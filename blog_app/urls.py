from django.urls import path
from . import views

urlpatterns = [
    path("", views.PostsView.as_view(), name="posts-page"),
    path("<slug:slug>", views.PostDetailView.as_view(), name="detail-page"),
    path("comment/<slug:slug>", views.CommentView.as_view(), name="comment-view")
]