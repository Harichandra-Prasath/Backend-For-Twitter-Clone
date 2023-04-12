from django.shortcuts import render,HttpResponse

from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
from Base.models import Tweets,Comments,Likes,Bookmarks,Following
from django.contrib.auth import get_user_model
from .serializers import TweetSerializer,DetailTweetSerializer,TweetPostSerializer,AddCommentSerializer,AddlikeSerializer,UserSerializer,FollowerSerializer
from .permissions import IsOwnerorRead,IsOwner
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

class ShowTweets(generics.ListAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetSerializer

class DetailShowTweet(generics.RetrieveDestroyAPIView):
    permission_classes = (IsOwnerorRead,)
    queryset = Tweets.objects.all()
    serializer_class = DetailTweetSerializer

class PostTweet(generics.CreateAPIView):
    queryset = Tweets.objects.all()
    serializer_class = TweetPostSerializer

class Comment(generics.CreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = AddCommentSerializer
    
    lookup_url_kwarg = "tweet_id"
    def create(self, request, *args, **kwargs):
        lookup_url_kwarg = "tweet_id"
        tweet_id= self.kwargs.get(self.lookup_url_kwarg)
        print(tweet_id)
        tweet = Tweets.objects.get(pk=tweet_id)
        cust_data = {
            "comment":request.data['comment'],
            "commented_by":request.user.pk,
            "commented_on":tweet.pk
        }
        serializer = self.get_serializer(data=cust_data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data)

class Like(generics.CreateAPIView):
    queryset = Likes.objects.all()
    serializer_class = AddlikeSerializer

    lookup_url_kwarg = "tweet_id"
    def create(self, request, *args, **kwargs):
        lookup_url_kwarg = "tweet_id"
        tweet_id= self.kwargs.get(self.lookup_url_kwarg)
        tweet = Tweets.objects.get(pk=tweet_id)
        if tweet.likes.filter(liked_by = request.user).count() >= 1:
            return Response({"Error":"You already liked the post"})       
        cust_data = {
            "Isliked":request.data['Isliked'],
            "liked_by":request.user.pk,
            "liked_on":tweet.pk
        }
        serializer = self.get_serializer(data=cust_data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Response(serializer.data)


class ShowUsers(generics.ListAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class ShowDetailUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerorRead,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class ShowUserTweets(generics.ListAPIView):      
    lookup_url_kwarg = "user_id"
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        tweets = get_user_model().objects.get(pk=user_id).tweets.all()
        return tweets
    serializer_class = TweetSerializer

    
class ShowBookmark(generics.ListAPIView):
    permission_classes = (IsOwner,)
    lookup_url_kwarg = "user_id"
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)

        try:
            Bookmarks.objects.get(user=get_user_model().objects.get(pk=user_id)) 
        except ObjectDoesNotExist:
            Bookmarks.objects.create(user=get_user_model().objects.get(pk=user_id))
        
        tweets = get_user_model().objects.get(pk=user_id).Buser.bookmarks.all()
        return tweets  
    serializer_class = TweetSerializer

@api_view(["POST"])
def Addbookmark(request,**kwargs):
    tweet_id = kwargs.get("tweet_id")
    tweet = Tweets.objects.get(pk=tweet_id)
    try:
        Bookmarks.objects.get(user=request.user) 
    except ObjectDoesNotExist:
       bookmark =  Bookmarks.objects.create(user=request.user)
       bookmark.bookmarks.add(tweet)
       return Response({"message":"Succesfully added"})

    if tweet not in Bookmarks.objects.get(user=request.user).bookmarks.all():
        Bookmarks.objects.get(user=request.user).bookmarks.add(tweet)
        return Response({"message":"Succesfully added"})
    return Response({"Error":"Already in bookmarks"})

    

class Showfollowings(generics.ListAPIView):
    lookup_url_kwarg = "user_id"
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)

        try:
            Following.objects.get(user=get_user_model().objects.get(pk=user_id)) 
        except ObjectDoesNotExist:
            Following.objects.create(user=get_user_model().objects.get(pk=user_id))
        
        following = get_user_model().objects.get(pk=user_id).Fuser.following.all()
        print(following)
        return following
    serializer_class = UserSerializer

@api_view(["POST"])
def Addfollowing(request,**kwargs):
    user_id = kwargs.get("user_id")
    user = get_user_model().objects.get(pk=user_id)
    try:
            Following.objects.get(user=request.user) 
    except ObjectDoesNotExist:
           following =  Following.objects.create(user=request.user)
           following.following.add(user)
           return Response({"message":"Succesfully followed"})

    if user not in Following.objects.get(user=request.user).following.all():
        Bookmarks.objects.get(user=request.user).bookmarks.add(user)
        return Response({"message":"Succesfully followed"})
    return Response({"Error":"Already in Followers"})

class Showfollowers(generics.ListAPIView):
    lookup_url_kwarg = "user_id"
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        user =  get_user_model().objects.get(pk=user_id)
        followers = Following.objects.filter(following=user)
        return followers
    serializer_class = FollowerSerializer
