from django.contrib.auth.models import User, Group
from django.db import models


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def points(self):
        return self.post_like_count + self.comment_like_count

    @property
    def post_like_count(self):
        return sum(post.points for post in self.post_set.all())

    @property
    def comment_like_count(self):
        return sum(comment.points for comment in self.comment_set.all())

    @property
    def post_count(self):
        return self.post_set.all().count()

    @property
    def comment_count(self):
        return self.comment_set.all().count()

class Post(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    title = models.CharField(max_length=64)
    body = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def points(self):
        return sum((1 if post_like.like else -1) for post_like in self.postlike_set.all())

class PostLike(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    post = models.ForeignKey(Post, on_delete=models.RESTRICT)
    parent = models.ForeignKey('self', on_delete=models.RESTRICT)
    body = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def points(self):
        return sum((1 if comment_like.like else -1) for comment_like in self.commentlike_set.all())

class CommentLike(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.RESTRICT)
    comment = models.ForeignKey(Comment, on_delete=models.RESTRICT)
    like = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

