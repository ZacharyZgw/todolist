from django.db import models

# Create your models here.

class Todo(models.Model):
    todo_id = models.IntegerField(default=1)
    content = models.CharField(max_length=500)
    createtime = models.DateTimeField("data published")

