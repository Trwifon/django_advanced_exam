from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from FisherPoint.common.mixins import ReadonlyViewMixin

UserModel = get_user_model()


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'bio', 'avatar')


class ProfileCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email')


class ProfileUpdateForm(ProfileBaseForm):
    pass


class DeleteUserForm(ReadonlyViewMixin, ProfileBaseForm):
    read_only_fields = ('username', 'first_name', 'last_name', 'bio', 'avatar')



