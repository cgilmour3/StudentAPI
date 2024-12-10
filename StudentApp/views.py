from django.shortcuts import render
from StudentApp.models import Student
from StudentApp.serializer import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def GetStudents(request):
    students = Student.objects.all()
    serialize = StudentSerializer(students, many=True)
    return Response(serialize.data)

@api_view(['GET', 'PUT', 'DELETE'])
def ModifyStudent(request,cnumber):
    try:
        students = Student.objects.get(cnumber=cnumber)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serialize = StudentSerializer(students)
        return Response(serialize.data)
    elif request.method == 'DELETE':
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == "PUT":
        serialize = StudentSerializer(students,data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response(serialize.data)
        else:
            return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def CreateStudent(request):
    serialize = StudentSerializer(data = request.data)
    if serialize.is_valid():
        serialize.save()
        return Response(serialize.data,status=status.HTTP_201_CREATED)
    else:
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)