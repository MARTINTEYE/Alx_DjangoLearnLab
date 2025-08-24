from django.urls import path
from api_project.api import views
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet
from .views import LikePostView, UnlikePostView

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = router.urls


urlpatterns = [
    path("feed/", views.user_feed, name="user-feed"),
]
urlpatterns = [
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
]