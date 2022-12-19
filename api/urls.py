from django.urls import path, include
from . import views

urlpatterns = [
    path('<str:matrix>/<int:step>', views.DegreeView.as_view())
]
