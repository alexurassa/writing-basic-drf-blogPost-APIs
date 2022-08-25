from django.contrib.auth.models import User
from rest_framework import mixins as rest_mixins
from rest_framework import generics

from .serializers import UserSerializer

class UsersListAPIView(rest_mixins.ListModelMixin, generics.GenericAPIView):
    """
    Returns the users list
    """
    
    queryset = User.objects.order_by("username")
    serializer_class = UserSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
users_list_api_view = UsersListAPIView.as_view()


class UserDetailAPIView(rest_mixins.RetrieveModelMixin,
                        generics.GenericAPIView):
    """
        API that only retrieves the user details
    Returns: 
        the instance of the User
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
user_detail_api_view = UserDetailAPIView.as_view()
    
