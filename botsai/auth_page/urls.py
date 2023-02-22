from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', AuthPage.as_view(), name='login'),
    path('registration/', RegPage.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout'),
]