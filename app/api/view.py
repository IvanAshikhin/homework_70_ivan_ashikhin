from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializes import TaskSerializer
from webapp.models import Task


# class TaskCreateView(APIView):
#
#     def post(self, request, *args, **kwargs):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)


class TaskListView(APIView):

    def get(self, request, *args, **kwargs):
        objects = Task.objects.all()
        serializer = TaskSerializer(objects, many=True)
        return Response(serializer.data)


