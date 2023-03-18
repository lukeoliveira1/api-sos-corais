from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from soscorais.views import RegistrationViewSet
from administrators.views import AdministratorViewSet

router = routers.DefaultRouter()
router.register('Registration', RegistrationViewSet, basename='Registrations')
router.register('Administrators', AdministratorViewSet, basename='Administrators')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
