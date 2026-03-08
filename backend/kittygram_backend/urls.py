from cats.views import custom_users_view
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', custom_users_view, name='custom-users'),
]
