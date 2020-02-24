from django.db import models

class College(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    def __str__(self):
        return self.name
