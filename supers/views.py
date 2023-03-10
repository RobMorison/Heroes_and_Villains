from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SupersSerializer
from .models import Supers
from super_types.models import SuperTypes
from super_types.serializers import SuperTypesSerializer

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):
    if request.method == 'GET':

        super_type = request.query_params.get('type')
   
        queryset = Supers.objects.all()

        if super_type:
            queryset = queryset.filter(super_types__type = super_type)
            serializer = SupersSerializer(queryset, many=True)
            return Response(serializer.data)
        else:
            heroes = Supers.objects.filter(super_types__type = "Hero")
            hero_serializer = SupersSerializer(heroes, many=True)
            villains = Supers.objects.filter(super_types__type = "Villain")
            villain_serializer = SupersSerializer(villains, many=True)
            custom_response = {
                "Heroes": hero_serializer.data,
                "Villains": villain_serializer.data,
            }
            return Response(custom_response)
            



    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    

@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    supers = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(supers);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(supers, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        supers.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)