from django.contrib.auth import authenticate # type: ignore
from rest_framework.response import Response # pyright: ignore[reportMissingImports]
from rest_framework.views import APIView # pyright: ignore[reportMissingImports]
from rest_framework.authtoken.models import Token # pyright: ignore[reportMissingImports]
from rest_framework.permissions import IsAuthenticated # pyright: ignore[reportMissingImports]
from rest_framework import status # pyright: ignore[reportMissingImports]
from .serializers import RegisterSerializer, UserSerializer
from django.contrib.auth import get_user_model # pyright: ignore[reportMissingModuleSource]
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import CustomUser

User = get_user_model()

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data}, status=201)
        return Response(serializer.errors, status=400)

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user": UserSerializer(user).data})
        return Response({"error": "Invalid credentials"}, status=400)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def follow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.follow(target_user)
    return Response({"message": f"You are now following {target_user.username}"}, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def unfollow_user(request, user_id):
    target_user = get_object_or_404(CustomUser, id=user_id)
    request.user.unfollow(target_user)
    return Response({"message": f"You have unfollowed {target_user.username}"}, status=status.HTTP_200_OK)