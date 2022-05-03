from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics

# Create your views here.

# API view
# It'll allows to see all of the different rooms but
# actually create a room
class RoomView(generics.CreateAPIView):
