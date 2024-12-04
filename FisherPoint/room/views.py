from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, View
from FisherPoint.message.models import Message
from FisherPoint.mixins import GroupRequiredMixin
from FisherPoint.room.forms import RoomUpdateForm, RoomDeleteForm, RoomCreateForm
from FisherPoint.room.models import Room

class RoomCreateView(GroupRequiredMixin, CreateView):
    model = Room
    form_class = RoomCreateForm
    template_name = 'room/room_create.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')
    group_name = 'fishermen'

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class RoomDetailsView(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'room/room_details.html'
    context_object_name = 'messages'
    login_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['room'] = Room.objects.get(pk=self.kwargs['pk'])
        context['message_count'] = Message.objects.filter(room=self.kwargs['pk']).count()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        room_pk = self.kwargs.get('pk')
        message_set = queryset.filter(room__pk=room_pk)

        return message_set


class RoomUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Room
    form_class = RoomUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'room/room_update.html'
    success_url = reverse_lazy("dashboard")
    login_url = reverse_lazy('login')

    def test_func(self):
        room = get_object_or_404(Room, pk=self.kwargs['pk'])
        return self.request.user == room.host


class RoomDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Room
    form_class = RoomDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'room/room_delete.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        room = get_object_or_404(Room, pk=self.kwargs['pk'])
        authorization = self.request.user == room.host or self.request.user.has_perm('room.delete_room')
        return authorization


class LikeMessageView(LoginRequiredMixin, View):

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy('room_details', pk=self.kwargs['room_pk'])


    def post(self, request, *args, **kwargs):
        message = get_object_or_404(Message, pk=kwargs['pk'])

        if request.user not in message.likes.all():
            message.likes.add(request.user)
        else:
            message.likes.remove(request.user)
        message.save()

        referer = request.META.get('HTTP_REFERER', '/')
        return HttpResponseRedirect(referer)
