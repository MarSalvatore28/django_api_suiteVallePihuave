from django.urls import path
from .views import LandingAPI
#landing
urlpatterns = [
    path('index/', LandingAPI.as_view(), name='landing-api-index'),
]