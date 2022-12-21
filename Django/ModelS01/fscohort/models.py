from django.db import models

# Create your models here.


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    number = models.IntegerField(default=0000)
    about = models.TextField(blank=True, null=True)
    register = models.DateTimeField(auto_now_add=True) # tarih ve zaman create edildiğinde
    last_updated_date = models.DateTimeField(auto_now=True) # tarih ve zaman yenileme
    is_active = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.number}  {self.first_name}"
    
    class Meta:
        ordering = ["number"]
        verbose_name_plural = "Student_list"

    def student_year_status(self):
        "Returns the student's year status"
        import datetime
        if self.register < datetime.date(2019, 1, 1):
            return "Senior"
        if self.register > datetime.date(2019, 1, 1):
            return "Junior"
        else:
            return "Freshman"