from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.order.models import Order, OrderDetail

from .serializers import OrderCreateSerializer, OrderSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = dict(
        pickup_location=["icontains"],
        dropoff_location=["icontains"],
        pickup_date=["exact"],
        order_date=["exact"],
    )
    ordering = "-created_at"

    def get_serializer_class(self):
        if self.action == "create":
            return OrderCreateSerializer
        return self.serializer_class

    def create(self, request):
        serializer_cls = self.get_serializer_class()
        serializer = serializer_cls(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = Order.objects.create(
            car_id=serializer.validated_data["car"],
            order_date=serializer.validated_data["order_date"],
            pickup_date=serializer.validated_data["pickup_date"],
            dropoff_date=serializer.validated_data["dropoff_date"],
            pickup_location=serializer.validated_data["pickup_location"],
            dropoff_location=serializer.validated_data["dropoff_location"],
        )

        OrderDetail(
            order=order,
            name=serializer.validated_data["name"],
            email=serializer.validated_data["email"],
            phone=serializer.validated_data["phone"],
        ).save()

        return Response(status=status.HTTP_201_CREATED, data=dict(order_id=order.id))
