from django.urls import path

from FisherPoint.common.views import index, Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]