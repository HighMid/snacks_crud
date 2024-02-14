from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    purchaser = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(get_user_model(), related_name='reviewer', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name