from django.contrib import admin
from django.db import models

from common.util.base_model import BaseModelMixin

# Create your models here.


class Article(BaseModelMixin):

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True)

    class Meta:
        db_table = "article"


admin.site.register(Article)
