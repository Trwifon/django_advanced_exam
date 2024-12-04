from django.urls import path, include
from FisherPoint.competition.views import CompetitionCreateView, CompetitionDetailView, \
    CompetitionUpdateView, CompetitionDeleteView

urlpatterns = [
    path('create/', CompetitionCreateView.as_view(), name='create_competition'),
    path('<int:pk>/', include([
        path('details/', CompetitionDetailView.as_view(), name='details_competition'),
        path('update/', CompetitionUpdateView.as_view(), name='update_competition'),
        path('delete/', CompetitionDeleteView.as_view(), name='delete_competition'),
    ]))
]
