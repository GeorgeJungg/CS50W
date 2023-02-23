from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("Daniel", views.Daniel, name="Daniel"),
    path("<str:name>", views.greet, name="greet")
]
