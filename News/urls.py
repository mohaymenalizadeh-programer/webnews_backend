from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'newsoftheday', views.NewsofthedayViewSet, basename='news_today')
router.register(r'lifestyle', views.NewsLifestyleViewSet, basename='lifestyle_news')
router.register(r'decoration', views.NewsDecorationViewSet, basename='decoration_news')
router.register(r'technology', views.NewsTechnologyViewSet, basename='technology_news')
router.register(r'artculture', views.NewsArtcultureViewSet, basename='artculture_news')
router.register(r'slidernews', views.NewsSlidernewsViewSet, basename='slidernews_news')
router.register(r'sliderstxt', views.SliderstxtViewSet, basename='slidertext')
router.register(r'comments', views.NewsComentViewSet, basename='comments')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', views.ListApiview.as_view(), name='list_news'),
    path('single/', views.SingleNewsView.as_view(), name='single_news'),
]