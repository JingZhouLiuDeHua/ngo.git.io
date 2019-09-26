from django.shortcuts import render

# Create your views here.
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])
def order_list(request):
    if request.method == 'GET':
        order=Order.objects.all()
        serializer=OrderSerializer(order,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def order_detail(request,pk):
    try:
        order=Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        order_detail=Order.objects.get(pk=pk)
        serializer=OrderSerializer(order_detail)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=OrderSerializer(order,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method=='DELETE':
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)