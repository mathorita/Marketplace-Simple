from django.contrib import admin
from django.urls import path,include
from market.views import OrderViewSet,ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('products',ProductViewSet,basename='products')
router.register('orders',OrderViewSet,basename='orders')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
