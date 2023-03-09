from django.db.models import Count, Sum, Max, Min, Avg
from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
import json
from django.http import HttpResponse

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
    # queryset = Order.objects.all().order_by('orderdate')
    serializer_class = OrderSerializer

    # @action(methods=['get'], detail=False)
    def get_queryset(self):
        request = self.request.query_params.get('orderdate')  # Запрос с одним параметром
        if not request:
            between_beg = self.request.query_params.get('between_beg')  # Тут запрашивают параметры фильтра по времени
            between_end = self.request.query_params.get('between_end')
            if between_beg is None and between_end is None:
                doiwantsum = self.request.query_params.get('sumflag')  # запросим наличие флага суммы
                if doiwantsum:

                    return Order.objects.all().aggregate(Sum('ordercost'))
                    #  Order.objects.all().annotate(Min('ordercost')) # Возвращает кверисет с [] со всеми записями

                    #  Order.objects.all().aggregate(Min('ordercost'))  #  AttributeError: Got AttributeError when attempting to get a value for field `ordernumber` on serializer `OrderSerializer`.
                                                                        #  The serializer field might be named incorrectly and not match any attribute or key on the `str` instance.
                                                                        #  Original exception text was: 'str' object has no attribute 'ordernumber'.

                   #  Order.objects.all().order_by('ordercost')        #  Возращает кверисет [] с всеми записями в порядке
                return Order.objects.all().order_by('orderdate')[:4]  # Выводит список если нет параметров
            else:
                between_beg = timezone.make_aware(datetime.strptime(between_beg, '%Y-%m-%d'), timezone.get_default_timezone())
                between_end = timezone.make_aware(datetime.strptime(between_end, '%Y-%m-%d'), timezone.get_default_timezone())
                return Order.objects.filter(orderdate__lte=between_end, orderdate__gte=between_beg)
        else:
            orderdate = timezone.make_aware(datetime.strptime(request, '%Y-%m-%d'), timezone.get_default_timezone())
            return Order.objects.filter(orderdate__day=orderdate.day, orderdate__month=orderdate.month, orderdate__year=orderdate.year)

    def get_sum(self):
        doiwantsum = self.request.query_params.get('sumflag')  # запросим наличие флага суммы
        if doiwantsum:
            return Order.objects.all().aggregate(Sum('ordercost'))


            # elif sumflag is not None:
            # return Order.objects.all().aggregate(Sum('ordercost'))
            # Order.objects.all().aggregate(Min('ordercost'))
            # Order.objects.all().aggregate(Max('ordercost'))
            # Order.objects.all().aggregate(Avg('ordercost'))
            # between_beg is not None and between_end is None:
            # return Order.objects.alias(entries=Count('ordercost'))

            #  Order.objects.values(analias2='ordernumber').annotate(analias=Count('pk')).order_by()
            #  Order.objects.order_by('ordercost')[:1]
            #  pubs = Order.objects.annotate(num_books=Count('book'))
            #  Order.objects.all().aggregate(Min('ordercost'))
            #  Order.objects.all().annotate(Min('ordercost'))
            #  Order.objects.all().order_by('ordercost')
            # return Order.objects.all().aggregate(total_price=Sum('ordercost'))  # должно выводить сумму?

