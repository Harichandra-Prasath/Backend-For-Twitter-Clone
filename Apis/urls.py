from django.urls import path
from .views import ShowTweets ,DetailShowTweet,PostTweet,Comment,Like,ShowUsers,ShowDetailUser,ShowUserTweets,AddBookmarks,ShowBookmark

urlpatterns = [
    path("tweets/" , ShowTweets.as_view() ),
    path("tweets/<int:pk>/" , DetailShowTweet.as_view() ),
    path("post/" , PostTweet.as_view()),
    path("tweets/<int:pk>/postcomment/" , Comment.as_view() ),
    path("tweets/<int:pk>/putlike/" , Like.as_view() ),
    path("users/", ShowUsers.as_view() ),
    path("users/<int:pk>/", ShowDetailUser.as_view() ),
    path("users/<int:user_id>/tweets", ShowUserTweets.as_view() ),
    path("users/<int:user_id>/Bookmark", ShowBookmark.as_view() ),
    path("tweets/<int:tweet_id>/addbookmark", AddBookmarks.as_view() )
    
]       