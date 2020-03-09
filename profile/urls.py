from django.conf.urls import url

from profile.views import UserProfileView

urlpatterns = [
    url(r'^profile', UserProfileView.as_view()),
    ]
