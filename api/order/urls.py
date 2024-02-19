from django.urls import path

from .views import OrderViewset

urlpatterns = [
    path("order/add/", OrderViewset.as_view(dict(post="create"))),
    path("order/list/", OrderViewset.as_view(dict(get="list"))),
    path(
        "order/<int:id>/",
        OrderViewset.as_view(dict(get="retrieve", post="update", delete="destroy")),
    ),
]
