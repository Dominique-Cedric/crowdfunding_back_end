from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    #password hasing (create user)
    def create(self, validated_data):
        #print(validated_data)
        return CustomUser.objects.create_user(**validated_data)