from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin

from FisherPoint.common.mixins import ReadonlyViewMixin
from FisherPoint.message.models import Message


class MessageBaseForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']

class MessageCreateForm(LoginRequiredMixin, MessageBaseForm):
    pass

class MessageDeleteForm(ReadonlyViewMixin, MessageBaseForm):
    read_only_fields = ('body',)

class MessageUpdateForm(LoginRequiredMixin, MessageBaseForm):
    pass

