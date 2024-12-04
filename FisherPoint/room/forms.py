from django import forms
from FisherPoint.mixins import ReadonlyViewMixin
from FisherPoint.room.models import Room


class RoomBaseForm(forms.ModelForm):
    name = forms.CharField(
        max_length=50,
        help_text='Enter the name of the room',
        widget=forms.TextInput(attrs={'placeholder': 'Room name'})
    )

    description = forms.CharField(
        help_text='Describe your room',
        widget=forms.Textarea(attrs={'placeholder': 'Room description'})
    )

    class Meta:
        model = Room
        fields = ['name', 'description']


class RoomCreateForm(RoomBaseForm):
    pass


class RoomUpdateForm(RoomBaseForm):
    pass


class RoomDeleteForm(ReadonlyViewMixin, RoomBaseForm):
    read_only_fields = ('name', 'description')