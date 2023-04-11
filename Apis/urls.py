from django.urls import path
from .views import ShowTweets ,DetailShowTweet,PostTweet,Comment,Like,ShowUsers,ShowDetailUser,ShowUserTweets,ShowBookmark,Addbookmark


urlpatterns = [
    path("tweets/" , ShowTweets.as_view() ),
    path("tweets/<int:pk>/" , DetailShowTweet.as_view() ),
    path("post/" , PostTweet.as_view()),
    path("tweets/<int:tweet_id>/postcomment/" , Comment.as_view() ),
    path("tweets/<int:tweet_id>/putlike/" , Like.as_view() ),
    path("users/", ShowUsers.as_view() ),
    path("users/<int:pk>/", ShowDetailUser.as_view() ),
    path("users/<int:user_id>/tweets", ShowUserTweets.as_view() ),
    path("users/<int:user_id>/bookmark", ShowBookmark.as_view() ),
    path("tweets/<int:tweet_id>/addbookmark/" , Addbookmark ),
]       