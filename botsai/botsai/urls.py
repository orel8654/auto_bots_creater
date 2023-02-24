from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('general_page.urls')),
    path('account/', include('auth_page.urls')),
    path('payment/', include('payment.urls')),
    path('editor/', include('editor.urls')),
    path('api/v1/', include('general_rest_api.urls')),
]