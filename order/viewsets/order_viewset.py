from rest_framework.viewsets import ModelViewSet

from order.models import Order
from order.serializers.order_serializer import OrderSerializer

class OrdertViewSet(ModelViewSet):    
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by('id')