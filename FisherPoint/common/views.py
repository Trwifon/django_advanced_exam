from django.db.models import Max
from django.shortcuts import render
from django.views.generic import ListView
from FisherPoint.competition.models import Competition
from FisherPoint.room.models import Room


def index(request):
    return render(request, 'common/index.html')

class Dashboard(ListView):
    model = Room
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        search_query = self.request.GET.get('query', '')

        room_count = Room.objects.all().count()
        rooms = (Room.objects.filter(name__icontains=search_query)
                 .annotate(latest_message=Max('room_messages__created_at'))
                 .order_by('-latest_message'))

        competition_count = Competition.objects.count()
        competitions = (Competition.objects.filter(title__icontains=search_query)
                        .order_by('-date_of_event'))

        return {'room_count': room_count,
                'rooms': rooms,
                'competition_count':competition_count,
                'competitions': competitions
                }
