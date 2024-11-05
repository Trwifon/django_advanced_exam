from django.contrib import admin
from django.urls import path, include

from FisherPoint import common

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FisherPoint.common.urls')),
    # path('account/', account.urls),
]
