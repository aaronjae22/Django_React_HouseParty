# It'll translate the attributes from the models to a json response
from rest_framework import serializers
from .models import Room

# Even though id is not defined in the Model Class,
# there is a automatically id field on every single Model.

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 
            'code', 
            'host', 
            'guest_can_pause', 
            'votes_to_skip',
            'created_at')