from .models import Department,Personnel
from .serializers import DepartmentSerializer
from .permissions import IsStafforReadOnly
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from rest_framework import generics

class DepartmentView(generics.ListCreateAPIView):
    serializer_class = DepartmentSerializer
    queryset = Department.objects.all()
    permission_classes = [IsAuthenticated,IsStafforReadOnly]

