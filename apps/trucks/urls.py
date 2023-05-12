from django.urls import path, include

from apps.trucks.views import TrucksView

app_name = 'trucks'

urlpatterns = [
    path('', TrucksView.as_view(), name='trucks')
]
