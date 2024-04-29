from django.shortcuts import render
from rest_framework import permissions, viewsets
from .models import Subscriber
from .serializers import SubscriberSerializer
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class SubscriberViewSet(viewsets.ModelViewSet):
    queryset = Subscriber.objects.all()
    serializer_class = SubscriberSerializer

    def get_serializer(self, *args, **kwargs):
        print(self)
        print(args)
        # print(kwargs)
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        kwargs.setdefault('context', self.get_serializer_context())
        return serializer_class(*args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        existing_subscriber = self.queryset.filter(email=email).first()
    
        if existing_subscriber:
            serializer = self.get_serializer(existing_subscriber, data=request.data)
        else:
            serializer = self.get_serializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)