from django.db.models import Count
from django.db.models import Q
from django.db.models import Avg
from django.shortcuts import render
import json

# Create your views here.

from rest_framework.decorators import action
from datetime import datetime
from django.utils import timezone

from rest_framework import viewsets

from TheApp.serializers import BuyerSerializer
from TheApp.models import Buyer

from TheApp.serializers import WorkerSerializer
from TheApp.models import Worker

from TheApp.serializers import ProviderSerializer
from TheApp.models import Provider

from TheApp.serializers import WarehouseSerializer
from TheApp.models import Warehouse

from TheApp.serializers import DeliveryCompanySerializer
from TheApp.models import DeliveryCompany

from TheApp.serializers import DeliverySerializer
from TheApp.models import Delivery

from TheApp.serializers import GenresSerializer
from TheApp.models import Genres

from TheApp.serializers import BookSerializer
from TheApp.models import Book

from TheApp.serializers import OrderSerializer
from TheApp.models import Order

from TheApp.serializers import AuthorSerializer
from TheApp.models import Author


class BuyerViewSet(viewsets.ModelViewSet):
    """
    API endpoint, который позволяет просматривать и редактировать
    """
    # queryset всех пользователей для фильтрации по дате последнего изменения
    queryset = Buyer.objects.all().order_by('pk')
    serializer_class = BuyerSerializer # Сериализатор для модели


class WorkerViewSet(viewsets.ModelViewSet):
    queryset = Worker.objects.all().order_by('name')
    serializer_class = WorkerSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all().order_by('name')
    serializer_class = WarehouseSerializer


class DeliveryCompanyViewSet(viewsets.ModelViewSet):
    queryset = DeliveryCompany.objects.all().order_by('name')
    serializer_class = DeliveryCompanySerializer


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all().order_by('orderid')
    serializer_class = DeliverySerializer


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all().order_by('genre')
    serializer_class = GenresSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
    #queryset = Order.objects.all().order_by('orderdate')
    serializer_class = OrderSerializer

    # @action(methods=['get'], detail=False)
    def get_queryset(self):
        request = self.request.query_params.get('orderdate')
        if not request:
            between_beg = self.request.query_params.get('between_beg')
            between_end = self.request.query_params.get('between_end')
            if between_beg is None and between_end is None:
                return Order.objects.all().order_by('orderdate')[:4]
            else:
                between_beg = timezone.make_aware(datetime.strptime(between_beg, '%Y-%m-%d'), timezone.get_default_timezone())
                between_end = timezone.make_aware(datetime.strptime(between_end, '%Y-%m-%d'), timezone.get_default_timezone())
                answer = Order.objects.filter(orderdate__lte=between_end, orderdate__gte=between_beg)#просто фильтрует по дате
                answer = Order.objects.alias(Count('ordercost')).filter(orderdate__lte=between_end, orderdate__gte=between_beg)#не работает
                return answer
                    #.filter(orderdate__lte=between_end, orderdate__gte=between_beg)
                    #Book.objects.aggregate(Avg('price'))
                    #bullshit#Order.objects.aggregate(Count('orderdate')).filter(orderdate__lte=between_end, orderdate__gte=between_beg)
                    #WORKS#Order.objects.filter(orderdate__lte=between_end, orderdate__gte=between_beg)
                #blogs = Blog.objects.alias(entries=Count('entry')).filter(entries__gt=5)
                #blogs = Blog.objects.aggregate(Count('orders')).filter(entries__gt=5)
                #TopCountries.objects.aggregate(Count('top_countries'))

        else:
            orderdate = timezone.make_aware(datetime.strptime(request, '%Y-%m-%d'), timezone.get_default_timezone())
            return Order.objects.filter(orderdate__day=orderdate.day, orderdate__month=orderdate.month, orderdate__year=orderdate.year)

