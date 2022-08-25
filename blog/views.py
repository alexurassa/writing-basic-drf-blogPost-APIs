from django.http import Http404
from rest_framework import mixins as rest_mixins, permissions
from rest_framework.generics import GenericAPIView

from .models import Post, PostCategory, PostComment
from .serializers import PostCommentSerializer, PostSerializer, PostCategorySerializer, PostTagSerializer


class PostCategoriesListAPIView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, GenericAPIView
):

    """API that:
        - returns the PostCategories
        - Create a new PostCategory

    Returns:
        rest-response: with get() and post() requests
    """

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


post_categories_list_api_view = PostCategoriesListAPIView.as_view()


class PostCategoryDetailAPIView(
    rest_mixins.RetrieveModelMixin,
    rest_mixins.UpdateModelMixin,
    rest_mixins.DestroyModelMixin,
    GenericAPIView,
):

    """
    -----------------------------------------
    Returns:
        get(request, *args, **kwargs) |
        put(request, *args, **kwargs) |
        destroy(request, *args, **kwargs)
    --------------------------------
    """

    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


post_category_detail_api_view = PostCategoryDetailAPIView.as_view()


class PostsListAPIView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, GenericAPIView
):

    """API that:
        - returns the list of all posts starting with the latest
        - Create a new post

    Returns:
        rest-response: with get() and post() requests
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


posts_list_api_view = PostsListAPIView.as_view()


class PostDetailAPIView(
    rest_mixins.RetrieveModelMixin,
    rest_mixins.UpdateModelMixin,
    rest_mixins.DestroyModelMixin,
    GenericAPIView,
):

    """
    -----------------------------------------
       API that get a specific Post instance to
       - get details
       - update/make changes
       - delete individual post
    --------------------------------
    """

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


post_detail_api_view = PostDetailAPIView.as_view()


class PostCommentListAPIView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, GenericAPIView):
    
    serializer_class = PostCommentSerializer
        
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_queryset(self):
        path = self.request.path 
        postId = path.split("/")[-3]
        comments_qs = PostComment.objects.filter(
            post__id = postId)
        return comments_qs
    
post_comment_list_api_view = PostCommentListAPIView.as_view()


class PostTagListAPIView(
    rest_mixins.ListModelMixin, rest_mixins.CreateModelMixin, GenericAPIView):
    
    serializer_class = PostTagSerializer
    queryset = PostComment.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
post_tag_list_api_view = PostTagListAPIView.as_view()


class PostTagDetailAPIView(
    rest_mixins.RetrieveModelMixin, 
    rest_mixins.UpdateModelMixin, 
    rest_mixins.DestroyModelMixin, 
    GenericAPIView
    ):
    
    serializer_class = PostTagSerializer
    queryset = PostComment.objects.all()
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
post_tag_detail_api_view = PostTagDetailAPIView.as_view()
