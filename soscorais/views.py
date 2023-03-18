from rest_framework import viewsets

from soscorais.models import registration
from soscorais.serializer import RegistrationSerializer

#filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = registration.objects.all()
    serializer_class = RegistrationSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter,SearchFilter]
    ordering_fields = ['nameArticle']
    search_fields = ['nameArticle', 'nameStudentOne', 'nameAdvisorOne']

