from django.urls import path, include
from FisherPoint.message.views import MessageUpdateView, MessageCreateView, MessageDeleteView
from FisherPoint.room.views import LikeMessageView

urlpatterns = [
    path('', include([
        path('create/', MessageCreateView.as_view(), name="create_message"),
        path('update/', MessageUpdateView.as_view(), name='update_message'),
        path('delete/', MessageDeleteView.as_view(), name='delete_message'),
        path('like/', LikeMessageView.as_view(), name='like_message'),
    ]))
]



