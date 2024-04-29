from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Subscriber
from .serializers import SubscriberSerializer
# Create your views here.

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer