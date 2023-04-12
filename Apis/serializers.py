from rest_framework import serializers
from django.contrib.auth import get_user_model
from Base.models import Comments,Likes,Tweets,Following


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
        model = Comments
        fields = ('comment' , 'commented_by',)

class AddCommentSerializer(serializers.ModelSerializer):
    #commented_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Comments
        fields = "__all__"

class AddlikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = "__all__"


class LikeSerializer(serializers.ModelSerializer):
    liked_by = serializers.SlugRelatedField(
        many=False,
        read_only = True,
        slug_field='username'
    )   

    class Meta:
        model = Likes
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

class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Following
        fields = ('user',)

