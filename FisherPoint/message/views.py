from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.context_processors import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, DeleteView, UpdateView

from FisherPoint.message.forms import MessageCreateForm, MessageDeleteForm
from FisherPoint.message.models import Message
from FisherPoint.room.models import Room


class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    form_class = MessageCreateForm
    template_name = 'message/message_create.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        room = Room.objects.get(pk=self.kwargs['pk'])
        form.instance.room = room
        room.participants.add(self.request.user)
        form.instance.user = self.request.user

        return super().form_valid(form)


class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    form_class = MessageCreateForm
    pk_url_kwarg = 'pk'
    template_name = 'message/message_update.html'
    success_url = reverse_lazy('dashboard')




class MessageDeleteView(DeleteView, FormView):
    model = Message
    form_class = MessageDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'message/message_delete.html'
    success_url = reverse_lazy('dashboard')


    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)


