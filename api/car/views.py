from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from api.car.models import Car

from .serializers import CarSerializer


class CarViewset(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = "id"
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = dict(
        name=["icontains"],
        location=["icontains"],
        start_date=["gte"],
        end_date=["lte"],
    )
    ordering = "-created_at"
