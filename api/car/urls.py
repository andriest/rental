from django.urls import path

from .views import CarViewset

urlpatterns = [
    path("car/add/", CarViewset.as_view(dict(post="create"))),
    path("car/list/", CarViewset.as_view(dict(get="list"))),
    path(
        "car/<int:id>/", CarViewset.as_view(dict(get="retrieve", post="update", delete="destroy"))
    ),
]
