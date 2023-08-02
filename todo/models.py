from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)


class TodoItem(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=False, auto_now=False)
    is_complete = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

