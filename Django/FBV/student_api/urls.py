from django.urls import path
from .views import (home, student_list,)
urlpatterns = [
    path("", home),
    path("student-list/", student_list, name='list'),
]
