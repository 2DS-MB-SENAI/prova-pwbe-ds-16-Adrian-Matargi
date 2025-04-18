from rest_framework import serializers
from .models import CustomUser

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'phone', 'address', 'birth_date', 'is_verified')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user