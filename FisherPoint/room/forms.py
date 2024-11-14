from django import forms

from FisherPoint.common.mixins import ReadonlyViewMixin
from FisherPoint.room.models import Room




class RoomBaseForm(forms.ModelForm):
    class Meta:
        model = Room
        exclude = ['host', 'participants']


class RoomCreateForm(RoomBaseForm):
    pass


class RoomUpdateForm(RoomBaseForm):
    pass


class RoomDeleteForm(ReadonlyViewMixin, RoomBaseForm):
    read_only_fields = ('name', 'description')