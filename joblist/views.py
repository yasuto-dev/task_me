from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .models import JobPost
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin

user = get_user_model()

#----仕事一覧ページ------
class JobPostView(ListView):
    model = JobPost
    template_name = "job_post_list.html"

    def get_queryset(self, **kwargs):
        queryset = super().get_queryset(**kwargs) # Article.objects.all() と同じ結果
        # GETリクエストパラメータにkeywordがあれば、それでフィルタする
        keyword = self.request.GET.get('keyword')
        if (keyword):
            queryset = queryset.filter(job_detail__icontains=keyword)

        return queryset
    
class JobRegistView(CreateView,LoginRequiredMixin):
    model = JobPost
    template_name = "job_regist.html"
    success_url = reverse_lazy("joblist:job_post_list")
    fields = ['job_title','job_detail']
    
    def form_valid(self, form):
        # ログインしているユーザーを取得し、それを紐づける
        form.instance.user = self.request.user
        form.instance.user_name = self.request.user.username
        return super().form_valid(form)

class JobUpdateView(UpdateView,LoginRequiredMixin):
    model = JobPost
    template_name = "job_update.html"
    success_url = reverse_lazy("joblist:job_post_list")
    fields = ['job_title','job_detail']
    pk_url_kwarg = 'pk'  # プライマリキーの名前を指定

class JobDeleteView(DeleteView,LoginRequiredMixin):
    model = JobPost
    template_name = "job_delete.html"
    success_url = reverse_lazy("joblist:job_post_list")
    fields = ['job_title','job_detail']
    pk_url_kwarg = 'pk'  # プライマリキーの名前を指定

