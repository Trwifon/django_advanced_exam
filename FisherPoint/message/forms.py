from django import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from FisherPoint.mixins import ReadonlyViewMixin
from FisherPoint.message.models import Message


class MessageBaseForm(forms.ModelForm):
    body = forms.CharField(
        help_text='Say something about your fishing hobby',
        widget=forms.Textarea(attrs={'placeholder': 'Message'})
    )

    class Meta:
        model = Message
        fields = ['body', 'image']

class MessageCreateForm(LoginRequiredMixin, MessageBaseForm):
    pass

class MessageDeleteForm(ReadonlyViewMixin, MessageBaseForm):
    read_only_fields = ('body',)

    class Meta:
        model = Message
        fields = ['body']
class MessageUpdateForm(LoginRequiredMixin, MessageBaseForm):
    pass
