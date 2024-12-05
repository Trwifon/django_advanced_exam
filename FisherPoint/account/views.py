from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, FormView, DeleteView
from FisherPoint.account.forms import ProfileCreateForm, ProfileUpdateForm, DeleteUserForm
from FisherPoint.account.helpers import get_competition_points, get_posts_number, get_fish_number
from FisherPoint.account.models import User
from FisherPoint.competition.models import Competition

UserModel = get_user_model()


class UserRegisterView(CreateView):
    model = UserModel
    form_class = ProfileCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        user=form.save()
        group=form.cleaned_data.get('group')
        user.groups.add(group)
        return super().form_valid(form)


class UserDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'account/profile_details.html'
    context_object_name = 'profile'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        profile = self.kwargs['pk']

        context['competition_points'] = get_competition_points(profile)
        context['posts'] = get_posts_number(profile)
        context['likes_total'] = get_fish_number(profile)
        context['competitions'] = Competition.objects.filter(participants=profile)

        return context


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = UserModel
    form_class = ProfileUpdateForm
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return self.request.user == user


class UserDeleteView(UserPassesTestMixin, DeleteView, FormView):
    model = UserModel
    form_class = DeleteUserForm
    template_name = 'account/profile_delete.html'
    success_url = reverse_lazy('dashboard')
    login_url = reverse_lazy('login')

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)

    def test_func(self):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        authorization = self.request.user == user or self.request.user.has_perm('account.delete_account')
        return authorization

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)