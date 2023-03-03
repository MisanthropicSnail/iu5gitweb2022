from django.db import models

# Create your models here.


class Buyer(models.Model):
    fullname = models.CharField(max_length=50, verbose_name="ФИО покупателя")
    address = models.CharField(max_length=100, verbose_name="Адрес покупателя")
    email = models.CharField(max_length=50, verbose_name="ЭлПочта покупателя")
    phone = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Телефон покупателя")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.fullname


class Worker(models.Model):
    name = models.CharField(max_length=50, verbose_name="ФИО Работника")
    job = models.CharField(max_length=50, verbose_name="Должность")

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название поставщика")

    def __str__(self):
        return self.name


class Warehouse(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название склада")

    def __str__(self):
        return self.name


class DeliveryCompany(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название Компании")

    def __str__(self):
        return self.name


class Delivery(models.Model):
    orderid = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Номер в доставке")
    deliverycompany = models.ForeignKey(DeliveryCompany, blank=True, null=True, on_delete=models.CASCADE)
    deliverydate = models.DateTimeField(auto_now=True, verbose_name="Дата доставки заказа в доставке")

    def __str__(self):
        return str(self.orderid) #преобразовываю в строку, иначе тут вылет


class Genres(models.Model):
    genre = models.CharField(max_length=50, verbose_name="Жанр книжки")

    def __str__(self):
        return self.genre


class Author(models.Model):
    name = models.CharField(max_length=80, verbose_name="Имя автора")

    def __str__(self):
        return self.name


class Book(models.Model):
    provider = models.ForeignKey(Provider, blank=True, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, blank=True, null=True, on_delete=models.CASCADE)
    warehouse = models.ManyToManyField(Warehouse)
    articul = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="Артикул")
    name = models.CharField(max_length=50, verbose_name="Название книжки")
    genres = models.ForeignKey(Genres, blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Ценник")

    def __str__(self):
        return self.name


class Order(models.Model):
    buyer = models.ForeignKey(Buyer, blank=True, null=True, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, blank=True, null=True, on_delete=models.CASCADE)
    deliverytype = models.ForeignKey(Delivery, blank=True, null=True, on_delete=models.CASCADE)
    ordernumber = models.DecimalField(max_digits=8, decimal_places=0, verbose_name="Номер заказа")
    orderdate = models.DateTimeField(auto_now=True, verbose_name="Дата заказа")
    orderstatus = models.DecimalField(max_digits=2, decimal_places=0, verbose_name="Статус заказа")
    deliverydate = models.DateTimeField(auto_now=True, verbose_name="Дата доставки заказа")
    ordercost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Стоимость заказа")
    books = models.ManyToManyField(Book)

    def __str__(self):
          return str(self.ordernumber)




