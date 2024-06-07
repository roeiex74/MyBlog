from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
from django.http import (
    HttpResponse,
    HttpResponseRedirect,
    Http404,
)
from django.urls import reverse
from django.template.defaultfilters import slugify
from datetime import date
from .models import Post, Author, Tag
from django.views.generic import ListView, DetailView, TemplateView
from django.views import View
from .forms import CommentForm

# Create your views here.


class HomePageView(ListView):
    template_name = "blog/home_page.html"
    model = Post
    ordering = ["-date", "title"]
    context_object_name = "latest_posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        # lazy hit
        data = queryset[:3]
        return data


# def home_page(request):
#     posts_query = Post.objects.all().order_by("-date", "title")[:3]
#     # This ^ is a one long sql query, with already sliced data - django optimization
#     # so django does not support negative slicing - we can play with the odrder_by clause

#     # sorted_posts_by_date = sorted(posts, key=get_post_date, reverse=True)
#     return render(request, "blog/home_page.html", {"latest_posts": posts_query})


class ListPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]


class DetailedPostView(View):
    def get(self, request, slug):
        selected_post = Post.objects.get(slug=slug)
        comments = selected_post.comments.all().order_by("-id")
        post_id = int(selected_post.id)
        stored_posts = request.session.get("stored_posts")
        saved_for_later = False if not stored_posts else post_id in stored_posts
        return render(
            request,
            "blog/post_data.html",
            {
                "post": selected_post,
                "tags": selected_post.tags.all(),
                "comment_form": CommentForm(),
                "comments": comments,
                "saved": saved_for_later,
            },
        )

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        selected_post = Post.objects.get(slug=slug)
        comment_succeed = comment_form.is_valid()
        if comment_succeed:
            # set commit false, to create an instance
            # that will be set to connect the post field to the comment
            comment_instance = comment_form.save(commit=False)
            comment_instance.post = selected_post
            comment_instance.save()

            return HttpResponseRedirect(reverse("post-data", args=[slug]))
        # Form is invalid - render with updated errors
        post_id = int(selected_post.id)
        stored_posts = request.session.get("stored_posts")
        saved_for_later = False if not stored_posts else post_id in stored_posts
        context = {
            "post": selected_post,
            "tags": selected_post.tags.all(),
            "comment_form": comment_form,
            "comments": selected_post.comments.all().order_by("-id"),
            "saved": saved_for_later,
        }
        return render(request, "blog/post_data.html", context)


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {"has_posts": False, "posts": []}

        if stored_posts and len(stored_posts) > 0:
            context["posts"] = Post.objects.filter(id__in=stored_posts)
            context["has_posts"] = True
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        action = request.POST.get("action")
        if action and action == "remove-selected":
            self.remove_selected(request)
        else:
            stored_posts = request.session.get("stored_posts")
            request.session["has_posts"] = True
            if not stored_posts:
                stored_posts = []

            post_id = int(request.POST["post_id"])
            if post_id not in stored_posts:
                stored_posts.append(post_id)

            request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/read-later")

    def remove_selected(self, request):
        selected_items = request.POST.getlist("selected_items")
        stored_posts = request.session.get("stored_posts")
        for post_id in selected_items:
            converted_post_id = int(post_id)
            if converted_post_id in stored_posts:
                stored_posts.remove(converted_post_id)
        request.session["stored_posts"] = stored_posts
        if len(stored_posts) == 0:
            request.session["has_posts"] = False


class PostsByTagView(ListView):
    template_name = "blog/post_tag.html"
    model = Post
    context_object_name = "posts"
    ordering = ["-date"]

    def get_queryset(self) -> QuerySet[Any]:
        selected_tag = Tag.objects.get(id=self.kwargs["tag_id"])
        posts = Post.objects.filter(tags=selected_tag)
        return posts

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs["tag_id"]
        print(tag_id)
        context["tag"] = Tag.objects.get(id=tag_id)
        return context


# def show_post(request, slug):
#     # post_data = Post.objects.filter(slug=slug)
#     # # post_data = next(post for post in posts if post["slug"] == slug)
#     # if not post_data:
#     #     raise Http404()
#     post_data = get_object_or_404(Post, slug=slug)
#     return render(
#         request,
#         "blog/post_data.html",
#         {"post": post_data, "tags": post_data.tags.all()},
#     )
