from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializes import TaskSerializer
from webapp.models import Task


class TaskUpdateView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class TaskListView(APIView):

    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)


class DetailTaskView(APIView):
    def get(self, request, pk):
        objects = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(objects)
        return Response(serializer.data)
