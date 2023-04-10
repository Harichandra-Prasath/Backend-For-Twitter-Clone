from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,response
from Base.models import Tweets,comments,likes
from django.contrib.auth import get_user_model
from .serializers import TweetSerializer,DetailTweetSerializer,TweetPostSerializer,AddCommentSerializer,AddlikeSerializer,UserSerializer,BookmarkSerializer
from .permissions import IsOwnerorRead,IsOwner

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
    queryset = comments.objects.all()
    serializer_class = AddCommentSerializer


class Like(generics.CreateAPIView):
    queryset = likes.objects.all()
    serializer_class = AddlikeSerializer

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


class AddBookmarks(APIView):
     lookup_url_kwarg = "tweet_id"
     def put(self, request, *args , **kwargs):  
        tweet_id = self.kwargs.get(self.lookup_url_kwarg)
        tweet = Tweets.objects.get(pk=tweet_id)
        data = request.data
        # this is the only field we want to update
        serializer = BookmarkSerializer(tweet, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return a meaningful error response
        return Response(serializer.errors, status=404)

    
class ShowBookmark(generics.ListAPIView):
    permission_classes = (IsOwner,)
    lookup_url_kwarg = "user_id"
    def get_queryset(self):
        user_id = self.kwargs.get(self.lookup_url_kwarg)
        tweets = get_user_model().objects.get(pk=user_id).bookmarks.all()
        return tweets  
    serializer_class = TweetSerializer
