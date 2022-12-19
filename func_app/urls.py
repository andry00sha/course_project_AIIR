from django.urls import path
from . import views

urlpatterns = [
    path('<str:matrix>/<int:step>', views.index)
]