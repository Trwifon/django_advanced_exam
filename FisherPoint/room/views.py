from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from FisherPoint.message.models import Message
from FisherPoint.room.forms import RoomUpdateForm, RoomDeleteForm
from FisherPoint.room.models import Room

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    template_name = 'room/room_create.html'
    fields = ['name', 'description']
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class RoomDetailsView(ListView):
    model = Message
    template_name = 'room/room_details.html'
    context_object_name = 'messages'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = Room.objects.get(pk=self.kwargs['pk'])
        context['room_count'] = Message.objects.filter(room=self.kwargs['pk']).count()

        return context


    def get_queryset(self):
        queryset = super().get_queryset()
        room_pk = self.kwargs.get('pk')
        message_set = queryset.filter(room__pk=room_pk)

        return message_set


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    form_class = RoomUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'room/room_update.html'
    success_url = reverse_lazy("dashboard")


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    form_class = RoomDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'room/room_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)





