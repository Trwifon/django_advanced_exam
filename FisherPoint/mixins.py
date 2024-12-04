from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden


class GroupRequiredMixin(LoginRequiredMixin):
    group_name = None

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)

        if self.group_name and not request.user.groups.filter(name=self.group_name).exists():
            return HttpResponseForbidden("You do not have permission to access this page.")

        return super().dispatch(request, *args, **kwargs)


class ReadonlyViewMixin:
    read_only_fields = []

    def make_fields_readonly(self):
        for field in self.read_only_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()