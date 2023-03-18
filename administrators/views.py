from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

from administrators.models import Administrator
from administrators.serializer import AdministratorSerializer

#filters
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    ordering_fields = ['username']
    search_fields = ['username']

class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return Response({'message': 'Por favor, informe o username e a senha'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            admin = Administrator.objects.get(username=username, password=password)
        except Administrator.DoesNotExist:
            return Response({'message': 'Credenciais inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response({'message': 'Login bem-sucedido'}, status=status.HTTP_200_OK)