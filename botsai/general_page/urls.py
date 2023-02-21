from django.urls import path
from .views import *

urlpatterns = [
    path('', GeneralPage.as_view()),
]