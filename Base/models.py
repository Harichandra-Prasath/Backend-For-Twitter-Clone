from django.db import models
from twitter.settings import AUTH_USER_MODEL

# Create your models here.

class Tweets(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="tweets")
    content = models.TextField(blank=False)

class Bookmarks(models.Model):
    user  = models.OneToOneField(AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="Buser")
    bookmarks = models.ManyToManyField(Tweets,blank=True,related_name="Btweets")

class Comments(models.Model):
    comment = models.TextField(blank=False)
    commented_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='commenter')
    commented_on = models.ForeignKey(Tweets , on_delete=models.CASCADE,related_name='comments')

class Likes(models.Model):
    Isliked = models.BooleanField(default=False)
    liked_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    liked_on = models.ForeignKey(Tweets , on_delete=models.CASCADE,related_name='likes')

class Following(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="Fuser")
    following = models.ManyToManyField(AUTH_USER_MODEL,blank=True,related_name="following")

    


