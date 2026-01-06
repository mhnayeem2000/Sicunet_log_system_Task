from django.shortcuts import render
from .models import AccessLog
from .serializers import AccessLogSerializer
from rest_framework import generics


class AccessLogViewSet(generics.ListCreateAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer

class AccessLogDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer    


