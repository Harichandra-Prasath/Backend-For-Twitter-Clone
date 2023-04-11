from django.contrib import admin
from .models import Tweets,Comments,Likes,Bookmarks

# Register your models here.
admin.site.register(Tweets)
admin.site.register(Comments)
admin.site.register(Likes)
admin.site.register(Bookmarks)
