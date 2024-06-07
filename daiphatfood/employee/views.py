# Create your views here.
# create employee aoi crud use django rest
from rest_framework import generics
from .serializers import RegisterSerializer
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from .models import Employee

class EmployeeList(generics.GenericAPIView):
    # serializer_class = RegisterSerializer
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return RegisterSerializer
        return EmployeeSerializer
    
    def get(self, request):
        employees = self.get_queryset()
        serializer = self.get_serializer(employees, many=True)
        data = serializer.data
        return Response(data)

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
