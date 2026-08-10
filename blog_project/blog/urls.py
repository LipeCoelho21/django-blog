from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),  # e.g., /
    path("all-posts/", views.all_posts, name="all-posts-page"),  # e.g., /all-posts/
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page"),  # e.g., /posts/first-post
]