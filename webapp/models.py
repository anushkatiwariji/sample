from django.db import models
from datetime import datetime
# Create your models here.

class Blog(models.Model):
    blog_id = models.AutoField(primary_key=True)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    about = models.TextField(max_length=200)
    date = models.DateField(default=datetime.now)
    def __str__(self):
        return f"{self.title}" 