from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView, UpdateView
from FisherPoint.message.forms import MessageCreateForm, MessageDeleteForm
from FisherPoint.message.models import Message
from FisherPoint.mixins import GroupRequiredMixin
from FisherPoint.room.models import Room

class MessageCreateView(GroupRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'message/message_create.html'
    group_name = 'fishermen'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        room = Room.objects.get(pk=self.kwargs['pk'])
        form.instance.room = room
        room.participants.add(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('room_details', kwargs={'pk': self.object.room.pk})


class MessageUpdateView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Message
    form_class = MessageCreateForm
    pk_url_kwarg = 'pk'
    template_name = 'message/message_update.html'
    login_url = reverse_lazy('login')

    def get_success_url(self):
        return reverse_lazy('room_details', kwargs={'pk': self.object.room.pk})

    def test_func(self):
        message = get_object_or_404(Message, pk=self.kwargs['pk'])
        return self.request.user == message.user


class MessageDeleteView(UserPassesTestMixin, DeleteView, FormView):
    model = Message
    form_class = MessageDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'message/message_delete.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        message = get_object_or_404(Message, pk=self.kwargs['pk'])
        authorization = self.request.user == message.user or self.request.user.has_perm('message.delete_message')
        return authorization
