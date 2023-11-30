from django.http import HttpResponse
from django.shortcuts import render, Http404, redirect, reverse
from django.views.generic import ListView, DetailView, View
from .models import PostModel, CommentPostModel
from .forms import CommentForm

# Create your views here.

class PostsView(ListView):
    template_name = "blog_app/posts_list.html"
    model = PostModel
    context_object_name = "posts"
    ordering = ["-created_date"]
    paginate_by = 2

    # def get_queryset(self):
    #     query = super(PostsView, self).get_queryset()
    #     data = query.all()[::-1]
    #     return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['url_page'] = 'blog'
        return context

class PostDetailView(DetailView):
    template_name = "blog_app/post_detail.html"
    model = PostModel
    context_object_name = "post"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.model.objects.all()
        context['recent_post'] = posts[:len(posts) - 4:-1]
        context['url_page'] = "post_detail"
        context['form'] = CommentForm()
        post: PostModel = posts.filter(slug__iexact=context["post"]).first()
        context['comments'] = post.post_comments.all()
        context["len_comments"] = len(context["comments"]) if len(context["comments"]) == 1 else "No"
        return context


class CommentView(View):
    def get(self, request):
        raise Http404()

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post: PostModel = PostModel.objects.filter(slug__iexact=slug).first()
        if comment_form.is_valid():
            if post is None:
                pass
            comment = CommentPostModel()
            comment.post = post
            comment.name = comment_form.cleaned_data.get("name")
            comment.email = comment_form.cleaned_data.get("email")
            comment.message = comment_form.cleaned_data.get("message")
            comment.save()

            return redirect(f"{reverse('posts-page')}{post.slug}")
