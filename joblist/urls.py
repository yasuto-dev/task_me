from django.urls import path
from . import views

app_name = "joblist"

urlpatterns = [
    path('',views.JobPostView.as_view(),name='job_post_list'),
    path('<int:pk>/update/',views.JobUpdateView.as_view(),name='job_update'),
    path('<int:pk>/delete/',views.JobDeleteView.as_view(),name='job_delete'),
    path('job_regist/',views.JobRegistView.as_view(),name='job_regist'),
]