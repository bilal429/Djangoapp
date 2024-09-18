from rest_framework import generics
from user.models import CustomUser
from .serializers import UserClassSerializer


class UserListView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserClassSerializer
