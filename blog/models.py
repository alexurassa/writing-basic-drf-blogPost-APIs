from django.db import models
from django.contrib.auth.models import User


class DatetimeMixin(models.Model):
    """
    Mixin that provide the createdAt and updatedAt datetimes
    """

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PostCategory(DatetimeMixin):
    """Each post should have a category"""

    name = models.CharField(max_length=100)
    description = models.TextField(max_length=300, null=True)

    def __str__(self):
        return f"{self.name}"


class Post(DatetimeMixin):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PostCategory, on_delete=models.SET_DEFAULT, default=1)
    overview = models.TextField(
        max_length=300, help_text="Gives the brief summary of a post"
    )
    content = models.TextField(max_length=1000, blank=False, default="Some content here")
    published = models.BooleanField(
        default=False, help_text="If set to true will be public visible"
    )
    publishedAt = models.DateTimeField(
        auto_now=True, null=True, blank=True, help_text="When published is set to True"
    )

    def __str__(self):
        return "%s" % (self.title)


class PostComment(DatetimeMixin):
    """
    --------------------------------------
    Model that retrieve user comment based on a particular Blog Post
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    email = models.EmailField(
        max_length=255, null=False, help_text="Helps to identify your comment"
    )
    content = models.TextField(
        max_length=300, help_text="What do you think of this post"
    )

    def __str__(self):
        return f"{self.email} commented at {self.createdAt}"


class PostTag(models.Model):
    title = models.CharField(max_length=100, help_text="important")
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField(max_length=250, null=True)

    def __str__(self):
        return f"{self.title} for {self.post.title}"
