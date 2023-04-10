from django.db import models
from twitter.settings import AUTH_USER_MODEL

# Create your models here.

class Tweets(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL , on_delete=models.CASCADE,related_name="tweets")
    content = models.TextField(blank=False)
    bookmarked_by = models.ManyToManyField(AUTH_USER_MODEL,related_name="bookmarks")

class comments(models.Model):
    comment = models.TextField(blank=False)
    commented_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='commenter')
    commented_on = models.ForeignKey(Tweets , on_delete=models.CASCADE,related_name='comments')

class likes(models.Model):
    Isliked = models.BooleanField(default=False)
    liked_by = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    liked_on = models.ForeignKey(Tweets , on_delete=models.CASCADE,related_name='likes')



    


