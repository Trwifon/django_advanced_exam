from django.urls import path, include

from FisherPoint.message.views import MessageCreateView
from FisherPoint.room.views import RoomCreateView, RoomDetailsView, RoomUpdateView, RoomDeleteView

urlpatterns = [
    path('create/', RoomCreateView.as_view(), name="create_room"),

    path('<int:pk>/', include([
        path('details/', RoomDetailsView.as_view(), name='room_details'),
        path('update/', RoomUpdateView.as_view(), name='room_update'),
        path('delete/', RoomDeleteView.as_view(), name='room_delete'),
    ]))
]
