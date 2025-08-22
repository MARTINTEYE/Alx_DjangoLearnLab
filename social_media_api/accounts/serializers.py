from rest_framework import serializers  # pyright: ignore[reportMissingImports]
from django.contrib.auth import get_user_model  # pyright: ignore[reportMissingModuleSource]
from rest_framework.authtoken.models import Token  # pyright: ignore[reportMissingImports]

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """Serializer for returning user data"""
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']


class RegisterSerializer(serializers.ModelSerializer):
    """Serializer for user registration"""
    # Ensure password is write-only so it never gets returned in API response
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        # Always use get_user_model() for creating users
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Automatically generate a token for the new user
        Token.objects.create(user=user)
        return user
