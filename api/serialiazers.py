from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from .models import *


class UserSerialiazer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'is_admin')
        # depth = 1
        
class StoriesSerializer(serializers.ModelSerializer):
    # image_url = serializers.ImageField(required=False)
    class Meta:
        model = Stories
        fields = '__all__'
        depth = 2
