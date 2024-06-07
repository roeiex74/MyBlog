from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePageView.as_view(), name="blog-home"),
    path("posts", views.ListPostsView.as_view(), name="all-posts"),
    path("posts/<slug:slug>", views.DetailedPostView.as_view(), name="post-data"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("tags/<int:tag_id>", views.PostsByTagView.as_view(), name="post-by-tag"),
]
