from django.shortcuts import render, HttpResponse, get_object_or_404

from .models import Student, Path

from .serializers import StudentSerializer, PathSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET'])  # default method GET
def home(request):
    return Response({'home': 'This is home page'})


#! ---------------------------HTTP methods -----------------------------------
# * ----GET() DB den veri çağırma public
# *----POST() DB de değişiklik create işlemi privatetır
# * ----PUT() DB den verilerde değişiklik için kullanılır privatetır  tüm field kısımlarını doldurmak zorundasın
# * doldurulmayan fieldlerde güncellenme ister.
# * ----DELETE() DB den veri silmek için kullanılır  privatetır
# * ----patch() DB de verilerde değişiklik için kullanılır ilgili field doldurmak yeterlidir o field güncellenir

@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    print('student', students)
    print("*************************")
    # ! db de birden fazla object geliyorsa many = True yazmamız gerek
    serializer = StudentSerializer(students, many=True)
    print("serializer", serializer)
    print("--------------------------------------------")

    print(serializer.data)
    return Response(serializer.data)
