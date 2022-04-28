from rest_framework import serializers
from .models import userProfile
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class userProfileSerializer(serializers.ModelSerializer):
    # user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = userProfile
        fields = '__all__'
