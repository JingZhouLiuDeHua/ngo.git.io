from django.shortcuts import render

# Create your views here.
from .models import Order
from rest_framework import viewsets
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('-date_joined')
    serializer_class = OrderSerializer