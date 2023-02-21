from django.urls import path
from .views import *

urlpatterns = [
    path('auth/', AuthPage.as_view()),
    path('registration/', RegPage.as_view()),
    path('succes/', SuccesReg.as_view()),
]