from rest_framework import serializers
from administrators.models import Administrator

class AdministratorSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    
    class Meta:
        model = Administrator
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}
