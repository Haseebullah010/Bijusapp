from django.urls import path

from .views import ReceiveImages

from . import views

urlpatterns = [
    path('', ReceiveImages.as_view()),
]