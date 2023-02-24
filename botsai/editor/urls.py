from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_required(Editor.as_view(), login_url='login'), name='editor'),
    path('template-creater/', login_required(CreaterTemplateTelegramBot.as_view(), login_url='login'), name='creatertp'),
]