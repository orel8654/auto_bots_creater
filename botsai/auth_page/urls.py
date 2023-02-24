from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', AuthPage.as_view(), name='login'),
    path('registration/', RegPage.as_view(), name='registration'),
    path('logout/', login_required(Logout.as_view(), login_url='login'), name='logout'),
]