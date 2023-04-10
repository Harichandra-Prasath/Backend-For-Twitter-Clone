from django.contrib import admin
from .models import Tweets,comments,likes

# Register your models here.
admin.site.register(Tweets)
admin.site.register(comments)
admin.site.register(likes)

