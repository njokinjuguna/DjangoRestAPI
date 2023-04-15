from rest_framework import serializers
from .models import DjangoDrink

class DjangoDrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model =DjangoDrink
        fields =['id','name','description']