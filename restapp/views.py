from django.shortcuts import render
from .models import Stock
from rest_framework import viewsets, filters
from .serializers import StockSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

# Create your views here.

class StockViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Stock.objects.all().order_by('stock_gain')
    serializer_class = StockSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    filter_fields = ('market_name',)
    search_fields = ('stock_name',)
    ordering = ('stock_gain',)

class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

