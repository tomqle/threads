from django.contrib.auth.models import User, Group

from backend.models import UserProfile, Post, PostLike, Comment, CommentLike

#-------------------- START User Profile --------------------#

def register_user(**kwargs):
    user = User.objects.create(**kwargs)
    UserProfile.objects.create(user=user)

#-------------------- END   User Profile --------------------#

#-------------------- START Post --------------------#

def create_post(**kwargs):
    post = Post.objects.create(**kwargs)


#-------------------- END   Post --------------------#

#-------------------- START Comment --------------------#
#-------------------- END   Comment --------------------#
