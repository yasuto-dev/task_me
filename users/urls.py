from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('profile_top/',views.TopView.as_view(),name='profile_top'),
    path('<int:pk>/profile_edit/',views.EditView.as_view(),name='profile_edit'),
]