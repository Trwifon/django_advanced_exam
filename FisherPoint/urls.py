from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FisherPoint.common.urls')),
    path('account/', include('FisherPoint.account.urls') ),
    path('room/', include('FisherPoint.room.urls') ),
    path('message/<int:pk>/', include('FisherPoint.message.urls') ),
]
