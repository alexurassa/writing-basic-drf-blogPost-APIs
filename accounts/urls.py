from django.urls import path 
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path("users/", users_list_api_view, name="users_list_view"),
    path("users/<int:pk>/detail/", user_detail_api_view, name="user_detail_view")
]
