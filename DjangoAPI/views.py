from django.http import JsonResponse
from .models import DjangoDrink
from .serializers import DjangoDrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request,format=None):
    #get all the drinks
    #serialize them
    #return json
    if request.method == 'GET':
        drinks = DjangoDrink.objects.all()
        serializer = DjangoDrinkSerializer(drinks,many=True)
        return Response(serializer.data)

    if request.method =='POST':
        serializer = DjangoDrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
@api_view(['GET','PUT','DELETE'])
def drink_detail(request,id,format=None):
    try:
       djangodrink= DjangoDrink.objects.get(pk=id)
    except DjangoDrink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer=DjangoDrinkSerializer(djangodrink)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = DjangoDrinkSerializer(djangodrink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        djangodrink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


