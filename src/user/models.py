from django.db import models

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'User'

    def __str__(self):
        return self.email