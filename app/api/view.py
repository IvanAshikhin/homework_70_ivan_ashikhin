from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializes import TaskSerializer, ProjectSerializer
from webapp.models import Task, Project


class TaskUpdateView(APIView):
    def put(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ProjectUpdateView(APIView):
    def put(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(project, data=request.data)
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


class DetailProjectView(APIView):
    def get(self, request, pk):
        objects = get_object_or_404(Project, pk=pk)
        serializer = ProjectSerializer(objects)
        return Response(serializer.data)


class DeleteView(APIView):
    def delete(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task_pk = task.pk
        task.delete()
        data = {'task_pk': task_pk}
        return Response(data)


class DeleteViewProject(APIView):
    def delete(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        tasks = Task.objects.filter(project=project)
        for task in tasks:
            task.project = None
            task.save()
        serializer = ProjectSerializer(project)
        project.delete()
        return Response(serializer.data)
