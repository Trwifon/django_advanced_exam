from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, FormView, DeleteView
from FisherPoint.account.forms import ProfileCreateForm, ProfileUpdateForm, DeleteUserForm

UserModel = get_user_model()

class UserRegisterView(CreateView):
    model = UserModel
    form_class = ProfileCreateForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('dashboard')


class UserDetailsView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'account/profile_details.html'
    context_object_name = 'profile'


class UserUpdateView(UpdateView):
    model = UserModel
    form_class = ProfileUpdateForm
    template_name = 'account/profile_update.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.avatar = form.data.get('avatar')
        return super().form_valid(form)


class UserDeleteView(DeleteView, FormView):
    model = UserModel
    form_class = DeleteUserForm
    template_name = 'account/profile_delete.html'
    success_url = reverse_lazy('dashboard')


    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)



