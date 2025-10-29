from django.db import models

# Create your models here.

class FavoriteCat(models.Model):
    breed_id = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    origen = models.CharField(max_length=100, null=True, blank=True)
    temperamento = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.breed_id})"
