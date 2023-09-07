from django.db import models

# Create your models here.
class Newsletter(models.Model):
    name = models.TextField(max_length=50)
    subscription = models.EmailField()

    def __str__(self):
        return self.name