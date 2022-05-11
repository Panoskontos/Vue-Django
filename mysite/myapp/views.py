from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
# Create your views here.

# @api_view(['GET'])
# def task_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         tasks_serializer = TaskSerializer(tasks, many=True)
#         return Response(tasks_serializer.data)

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()