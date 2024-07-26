from rest_framework import viewsets
from .models import Show
from .serializers import ShowSerializer
from rest_framework import  permissions


class ShowViewSet(viewsets.ModelViewSet):
    permission_classes=[permissions.AllowAny]
    queryset = Show.objects.all()
    serializer_class = ShowSerializer
