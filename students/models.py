from django.db import models
from django.contrib.auth.hashers import make_password

class students(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.BigIntegerField(null=True, blank=True)
    track = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Hash the password before saving
        self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
