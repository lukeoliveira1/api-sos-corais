from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from soscorais.views import RegistrationViewSet
from administrators.views import AdministratorViewSet, LoginView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="sos-corais API",
      default_version='v1',
      description="An API for sos-corais front-end",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sos-corais@email.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

router = routers.DefaultRouter()
router.register('Registration', RegistrationViewSet, basename='Registrations')
router.register('Administrators', AdministratorViewSet, basename='Administrators')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
