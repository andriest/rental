from rest_framework import serializers

from api.order.models import Order, OrderDetail


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        exclude = ["order", "id"]


class OrderCreateSerializer(serializers.Serializer):
    car = serializers.IntegerField(required=True)
    order_date = serializers.DateField(required=True)
    pickup_date = serializers.DateField(required=True)
    dropoff_date = serializers.DateField(required=True)
    pickup_location = serializers.CharField(max_length=50, required=True)
    dropoff_location = serializers.CharField(max_length=50, required=True)
    name = serializers.CharField(max_length=100, required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.CharField(max_length=20, required=True)


class OrderSerializer(serializers.ModelSerializer):
    order_detail = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = [
            "id",
            "car",
            "order_date",
            "pickup_date",
            "dropoff_date",
            "pickup_location",
            "dropoff_location",
            "order_detail",
        ]
        read_only_fields = ["created_at", "updated_at"]

    def get_order_detail(self, obj):
        detail = OrderDetail.objects.filter(order=obj).first()
        if detail:
            serializers = OrderDetailSerializer(detail)
            return serializers.data
        else:
            return None

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep.update(
            car=dict(
                id=instance.car.id,
                name=instance.car.name,
                image=instance.car.image,
                day_rate=instance.car.day_rate,
                created_at=instance.car.created_at,
            )
        )
        return rep
