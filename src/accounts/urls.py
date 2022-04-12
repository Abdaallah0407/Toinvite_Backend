
from lib2to3.pgen2 import token
from django.urls import path, include, re_path
from src.accounts.views import UserAPI, UserProfileView, UserOwnInActiveAdsView, UserOwnActiveAdsView, UserOwnUnPublishedAdsView


urlpatterns = [
    path('api/user/', UserAPI.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'api/auth/', include('djoser.urls.authtoken')),
    path('api/user/profile/<int:user_id>/',
         UserProfileView.as_view(), name="user_profile"),
    path('api/user/own/ads/active/', UserOwnActiveAdsView.as_view(),
         name="user_own_active_ads"),
    path('api/user/own/ads/inactive/', UserOwnInActiveAdsView.as_view(),
         name="user_own_inactive_ads"),
    path('api/user/own/ads/unpublished/', UserOwnUnPublishedAdsView.as_view(),
         name="user_own_unpublished_ads"),
]
