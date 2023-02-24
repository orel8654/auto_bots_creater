from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *

urlpatterns = [
    path('', login_required(Payment.as_view(), login_url='login'), name='qiwi_pay'),
    path('verify', login_required(Verify.as_view(), login_url='login'), name='verify'),
]