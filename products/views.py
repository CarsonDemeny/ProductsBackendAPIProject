from itertools import product
from urllib.request import Request
from rest_framework.decorators import api_view
from rest_framework.decorators import Response
from rest_framework import status

import products
from .serializers import ProductSerializer
from .models import Product
from products import serializers


@api_view(['GET', 'POST'])
def cars_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
