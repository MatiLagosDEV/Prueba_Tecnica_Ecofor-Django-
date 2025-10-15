from django.db import models

# Create your models here.

class Cat(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    temperamento = models.CharField(max_length=255)
    esperanza_vida = models.CharField(max_length=50)
    descripcion_completa = models.TextField()

    def __str__(self):
        return self.name
    

class favoriteCat(models.Model):
    id = models.AutoField(primary_key=True)
    cat = models.ForeignKey(Cat, on_delete=models.CASCADE)

    def __str__(self):
        return self.cat.name    
