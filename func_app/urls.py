from django.urls import  path
from . import views

urlpatterns = [
    path('<int:size>/<matrix>/<int:step>', views.degree)
]