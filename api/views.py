from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

            # API view

"""
It'll allows to see all of the different rooms but actually create a room

queryset will get the return of all of the Room objects
and the serializer_class will convert it into a format that can be returned
"""
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    
