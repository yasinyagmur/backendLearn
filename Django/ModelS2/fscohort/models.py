from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=25,blank=True)
    last_name = models.CharField(max_length=25)
    number = models.PositiveSmallIntegerField(blank=True,null=True)
    def __str__(self) -> str:
        return f"{self.number}- {self.first_name}"
    
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Students List"
        # db_table = "" tablo ismini değiştirir
