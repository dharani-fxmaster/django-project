from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentsSerializer, EmployeeSerializer
from students.models import Students
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employee.models import Employee

# Create your views here.
# Manual 
def StudentsViews(request):
    student = Students.objects.all()
    students_list = list(student.values())
    return JsonResponse(students_list, safe=False)

# With serializer methods
@api_view(['GET','POST'])
def StudentsViews(request):
    # get all  the data from students
    if request.method == 'GET':
         student = Students.objects.all()
         serializer = StudentsSerializer(student, many=True)
         return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST': 
        serializer = StudentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT', 'DELETE']) 
def StudentDetailView(request, pk):
    try:
        student =  Students.objects.get(pk=pk)
    except Students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
       serializer = StudentsSerializer(student)  
       return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
         serializer = StudentsSerializer(student, data=request.data) 
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         else: 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         student.delete()  
         return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'DELETE':
        student.delete()
        return Response(
            {"message": "Student deleted successfully"},
            status=status.HTTP_204_NO_CONTENT
        )
  

class Employees(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)    

    def post(self, request):  
        serializer = EmployeeSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EmployeeDetail(APIView):
    def get_object(self, pk):
        try:
          employees =  Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        employees = self.get_object(pk)   
        serializer = EmployeeSerializer(employees) 
        return Response(serializer.data, status=status.HTTP_200_OK)    

 
        