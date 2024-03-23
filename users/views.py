from django.http.response import HttpResponseRedirect
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login
from django.urls import reverse_lazy
from users.models import User


class TopView(TemplateView):
    template_name = "profile_top.html"
    model = User

class EditView(CreateView):
    model = User
    template_name = "profile_edit.html"
    success_url = reverse_lazy("users:profile_top")
    pk_url_kwarg = 'pk'  # プライマリキーの名前を指定

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.object = user
        return HttpResponseRedirect(self.get_success_url())
