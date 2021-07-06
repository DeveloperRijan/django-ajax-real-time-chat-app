from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField

# Create your models here.
class Group(models.Model):
    name=models.CharField(max_length=99)

class Message(models.Model):
    group = models.ForeignKey(
        Group,
        null=True,
        on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=SET_NULL
    )
    message=models.CharField(max_length=2000)
    created_at=models.DateTimeField(null=True)
    