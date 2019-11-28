
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Createa new use in the system"""
    serializer_class = UserSerializer
