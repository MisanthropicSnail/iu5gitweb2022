"""lab3e URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from TheApp import views as bookdel_views
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'buyers', bookdel_views.BuyerViewSet)
router.register(r'workers', bookdel_views.WorkerViewSet)
router.register(r'providers', bookdel_views.ProviderViewSet)
router.register(r'warehouses', bookdel_views.WarehouseViewSet)
router.register(r'delcomps', bookdel_views.DeliveryCompanyViewSet)
router.register(r'deliveries', bookdel_views.DeliveryViewSet)
router.register(r'genres', bookdel_views.GenresViewSet)
router.register(r'books', bookdel_views.BookViewSet)
router.register(r'authors', bookdel_views.AuthorViewSet)
router.register(r'orders', bookdel_views.OrderViewSet, basename='order')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]