from django.urls import path, include
from .views import Landing

urlpatterns = [
    path('', Landing.as_view(), name='Landing'),
]