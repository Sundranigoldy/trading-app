from django.db import models

# Create your models here.
class stock(models.Model):
    search = models.CharField(max_length=10)

    def __str__(self):
        return self.search