from cats.views import AchievementViewSet, CatViewSet, custom_users_view
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'achievements', AchievementViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', custom_users_view, name='custom-users'),
    path('api/', include(router.urls)),
    # path('api/', include('djoser.urls')),
    # path('api/', include('djoser.urls.authtoken')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
