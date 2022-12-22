from django.db import models

# Create your models here.


class Student(models.Model):
    firt_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    number = models.IntegerField(blank=True,null=True)
    age = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.firt_name}"