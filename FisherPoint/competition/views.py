from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models.expressions import result
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, FormView
from FisherPoint.competition.forms import (
    CompetitionCreateForm,
    CompetitionTakePartForm,
    CompetitionUpdateForm,
    CompetitionDeleteForm
)
from FisherPoint.competition.models import Competition
from FisherPoint.mixins import GroupRequiredMixin


class CompetitionCreateView(GroupRequiredMixin, CreateView):
    group_name = 'clubs'
    model = Competition
    form_class = CompetitionCreateForm
    template_name = 'competition/competition_create.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.host = self.request.user
        return super().form_valid(form)


class CompetitionDetailView(DetailView, FormView):
    model = Competition
    form_class = CompetitionTakePartForm
    template_name = 'competition/competition_details.html'
    context_object_name = 'competition'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_date'] = date.today()

        is_fishermen = self.request.user.groups.filter(name='fishermen').exists()
        context['is_fishermen'] = is_fishermen

        return context

    def form_valid(self, form):
        competition = get_object_or_404(Competition, pk=self.kwargs['pk'])
        competition.participants.add(self.request.user)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details_competition', kwargs={'pk': self.kwargs['pk']})


class CompetitionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Competition
    form_class = CompetitionUpdateForm
    pk_url_kwarg = 'pk'
    template_name = 'competition/competition_update.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def test_func(self):
        competition = get_object_or_404(Competition, pk=self.kwargs['pk'])
        return self.request.user == competition.host


class CompetitionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Competition
    form_class = CompetitionDeleteForm
    pk_url_kwarg = 'pk'
    template_name = 'competition/competition_delete.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        competition = get_object_or_404(Competition, pk=self.kwargs['pk'])
        authorization = self.request.user == competition.host or self.request.user.has_perm('competition.delete_competition')
        return authorization

