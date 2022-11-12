from django.urls import path 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from .views import (
    users_list_api_view,
    user_detail_api_view
)

app_name = "accounts"

urlpatterns = [
    path("users/", users_list_api_view, name="users_list_view"),
    path("users/<int:pk>/detail/", user_detail_api_view, name="user_detail_view"),
    
    # simple jwt routes
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
