from django.db import models


# Create your models here.

class airport(models.Model):
    code=models.CharField(max_length=5)
    city=models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code}) "

class flight(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="departure")
    destination=models.ForeignKey(airport,on_delete=models.CASCADE,related_name="arrival")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} to {self.destination} "

class passengers(models.Model):
    first=models.CharField(max_length=64)
    last=models.CharField(max_length=64)
    flight=models.ManyToManyField(flight,blank=True,related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last} "

