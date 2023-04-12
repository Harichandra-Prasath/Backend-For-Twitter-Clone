from django.urls import path
from .views import ShowTweets ,DetailShowTweet,PostTweet,Comment,Like,ShowUsers,ShowDetailUser,ShowUserTweets,ShowBookmark,Addbookmark,Showfollowings,Addfollowing,Showfollowers

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
    path("users/<int:user_id>/follow/", Addfollowing),
    path("users/<int:user_id>/followers/" , Showfollowers.as_view()),
    path("users/<int:user_id>/followings/" , Showfollowings.as_view())
]       