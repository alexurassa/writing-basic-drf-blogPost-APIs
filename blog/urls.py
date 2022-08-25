from django.urls import path
from blog.views import *

urlpatterns = [
    path(
        "posts/categories/",
        post_categories_list_api_view,
        name="post_categories_list_view",
    ),
    path(
        "posts/categories/<int:pk>/detail/",
        post_category_detail_api_view,
        name="post_category_detail_view",
    ),
    path("posts/", posts_list_api_view, name="post_list_view"),
    path("posts/<int:pk>/detail/", post_detail_api_view, name="post_detail_view"),
    path("<int:postId>/comments/", post_comment_list_api_view, name="post_comment_list_view"),
    path("tags/", post_tag_list_api_view, name="post_tag_list_view"),
    path("tags<int:pk>/", post_tag_detail_api_view, name="post_tag_detail_view")
]
