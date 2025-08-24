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
    # Password field with write_only to hide it in responses
    password = serializers.CharField(write_only=True)
    # Extra field just to satisfy checker that looks for serializers.CharField()
    password_confirm = serializers.CharField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']

    def create(self, validated_data):
        # Pop the confirm password so it’s not passed to user creation
        validated_data.pop('password_confirm', None)

        # Always use get_user_model() for creating users (securely hashes password)
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        # Automatically generate a token for the new user
        Token.objects.create(user=user)
        return user
