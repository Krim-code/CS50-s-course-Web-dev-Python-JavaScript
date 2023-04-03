from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Dashboard(models.Model):
    tasks = models.TextField()
    user = models.ForeignKey(User, blank=True, null=False,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tasks} from {self.user}"
