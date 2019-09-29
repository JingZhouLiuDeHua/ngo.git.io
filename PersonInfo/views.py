
from .models import PersonInfo
from rest_framework import viewsets
from .serializers import PersonInfoSerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def personinfo_list(request):
    if request.method == 'GET':
        personinfo=PersonInfo.objects.all()
        serializer=PersonInfoSerializer(personinfo,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=PersonInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def personinfo_detail(request,pk):
    try:
        personinfo=PersonInfo.objects.get(pk=pk)
    except PersonInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        personinfo_detail=PersonInfo.objects.get(pk=pk)
        serializer=PersonInfoSerializer(personinfo_detail)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=PersonInfoSerializer(personinfo,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        personinfo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)