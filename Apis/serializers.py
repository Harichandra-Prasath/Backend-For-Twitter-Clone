from rest_framework import serializers
from django.contrib.auth import get_user_model
from Base.models import comments,likes,Tweets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id','username' , 'first_name', 'last_name' , 'email' , 'date_joined',)

class CommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.SlugRelatedField(
            many = False,
            read_only = True,
            slug_field= 'username'
        )
    class Meta:
        model = comments
        fields = ('comment' , 'commented_by',)

class AddCommentSerializer(serializers.ModelSerializer):
    commented_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = comments
        fields = "__all__"

class AddlikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = likes
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.SlugRelatedField(
        many=False,
        read_only = True,
        slug_field='username'
    )   

    class Meta:
        model = likes
        fields = ('liked_by',)

class TweetPostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Tweets
        fields = ("id" , "user" , "content", )
    
        

class TweetSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field="username"
    )

    class Meta:
        model = Tweets
        fields = ('id' , 'user' , 'content',)


class DetailTweetSerializer(serializers.ModelSerializer):
   
    comments = CommentSerializer(many=True)

    user = serializers.SlugRelatedField(
        many = False,
        read_only = True,
        slug_field="username"
    )

    likes = LikeSerializer(many=True)
   
    class Meta:
        model = Tweets
        fields = ('user' , 'content' , 'comments','likes',)

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweets
        fields = ['bookmarked_by',]