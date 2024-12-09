from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from FisherPoint.mixins import ReadonlyViewMixin

UserModel = get_user_model()


class ProfileBaseForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=30,
        help_text='Enter your first name.',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}))

    last_name = forms.CharField(
        max_length=30,
        help_text='Enter your last name.',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))

    avatar = forms.FileField(
        required=False,
        help_text='Allowed types are: jpg, jpeg, png, gif, webp, jfif and file size must be below 0.5 MB'
    )

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'description', 'avatar')


class ProfileCreateForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        help_text= 'Your username must contain only letters, numbers, apostrophe and underscores.',
        widget=forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.EmailField(
        help_text='Enter your email address',
        widget=forms.TextInput(attrs={'placeholder': 'Email'}))

    group = forms.ModelChoiceField(
        queryset=Group.objects.exclude(name='moderator'),
        required=True,
        help_text='Choose your group',
    )

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'group')


class ProfileUpdateForm(ProfileBaseForm):
    pass


class DeleteUserForm(ReadonlyViewMixin, ProfileBaseForm):
    read_only_fields = ('username', 'first_name', 'last_name', 'description')

    class Meta:
        model = UserModel
        fields = ('username', 'first_name', 'last_name', 'description')


