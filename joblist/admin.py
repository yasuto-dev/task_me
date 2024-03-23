from django.contrib import admin
from .models import JobPost

class JobPostAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_name', 'job_title', 'job_detail','created_at')


admin.site.register(JobPost, JobPostAdmin)