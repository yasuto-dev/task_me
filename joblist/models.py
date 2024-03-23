from django.db import models
from users.models import User
from datetime import datetime


class JobPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name=("ユーザー"), on_delete=models.CASCADE)
    user_name = models.CharField(verbose_name="ユーザー名", max_length=50)
    job_title = models.CharField(verbose_name="仕事タイトル",max_length=255)
    job_detail = models.CharField(verbose_name="仕事詳細",max_length=1000)
    created_at = models.DateTimeField(verbose_name="登録日時", default=datetime.now)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True, blank=True, null=True)
    
    def __str__(self):
        return self.job_title
