from django import forms
from FisherPoint.account.models import User
from FisherPoint.mixins import ReadonlyViewMixin
from FisherPoint.competition.models import Competition


class CompetitionBaseForm(forms.ModelForm):
    title = forms.CharField(
        max_length=50,
        help_text='Must contains only letters, numbers and spaces',
        widget=forms.TextInput(attrs={'placeholder': 'Title'})
    )

    description = forms.CharField(
        help_text='Describe competition',
        widget=forms.Textarea(attrs={
            'placeholder': 'Describe competition - rules, fees, start time, awards, charity ...'
        })
    )

    location = forms.CharField(
        max_length=100,
        help_text='Where is the competition located?',
        widget=forms.TextInput(attrs={'placeholder': 'Place of the competition'})
    )

    date_of_event = forms.DateField(
        help_text='Date of the competition',
        widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
    )

    class Meta:
        model = Competition
        fields = ('title', 'description', 'location', 'date_of_event')


class CompetitionCreateForm(CompetitionBaseForm):
    pass


class CompetitionTakePartForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ()


class CompetitionUpdateForm(CompetitionBaseForm):
    class Meta:
        model = Competition
        fields = ('title', 'description', 'location', 'date_of_event',
                  'photo', 'first_place', 'second_place', 'third_place')

    def __init__(self, *args, **kwargs):
        super(CompetitionUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_place'].queryset = User.objects.filter(competition=self.instance)
        self.fields['second_place'].queryset = User.objects.filter(competition=self.instance)
        self.fields['third_place'].queryset = User.objects.filter(competition=self.instance)



class CompetitionDeleteForm(ReadonlyViewMixin, CompetitionBaseForm):
    read_only_fields = ['title', 'description', 'location', 'date_of_event']

