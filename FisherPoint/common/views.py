from django.shortcuts import render
from django.views.generic import ListView

from FisherPoint.message.models import Message
from FisherPoint.room.models import Room


def index(request):
    return render(request, 'common/index.html')

class Dashboard(ListView):
    model = Room
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        room_count = Room.objects.count()
        rooms = Room.objects.all()
        return {'room_count': room_count, 'rooms': rooms}