from django.shortcuts import render
from .models import AccessLog
from .serializers import AccessLogSerializer
from rest_framework import generics


class AccessLogViewSet(generics.ListCreateAPIView):
    serializer_class = AccessLogSerializer


    def get_queryset(self):
        queryset = AccessLog.objects.all().order_by('-timestamp')
        card_id = self.request.query_params.get('card_id', None)
        if card_id:
            queryset = queryset.filter(card_id=card_id)
        return queryset
    

class AccessLogDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessLog.objects.all()
    serializer_class = AccessLogSerializer    


