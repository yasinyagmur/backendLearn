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


# http methods -------->
# ----GET() DB den veri çağırma
