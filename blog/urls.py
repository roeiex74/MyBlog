from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="blog-home"),
    # path("/posts"),
    # path("/posts/<str:slug>", name="selected_post"),
]
