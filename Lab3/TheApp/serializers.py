from TheApp.models import Buyer
from TheApp.models import Worker
from TheApp.models import Provider
from TheApp.models import Warehouse
from TheApp.models import DeliveryCompany
from TheApp.models import Delivery
from TheApp.models import Genres
from TheApp.models import Author
from TheApp.models import Book
from TheApp.models import Order
from rest_framework import serializers


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Buyer
        # Поля, которые мы сериализуем
        fields = ["pk", "fullname", "address", "email", "phone"]


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields = ["pk", "name", "job"]


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ["pk", "name"]


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ["pk", "name"]


class DeliveryCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryCompany
        fields = ["pk", "name"]


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ["pk", "orderid", "deliverycompany", "deliverydate"]


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ["pk", "genre"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["pk", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["pk", "provider", "author", "warehouse", "articul", "name", "genres", "price"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["pk", "buyer", "worker", "deliverytype", "ordernumber", "orderdate", "orderstatus", "deliverydate", "ordercost", "books"]