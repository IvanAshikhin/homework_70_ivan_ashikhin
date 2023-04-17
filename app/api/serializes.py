from rest_framework import serializers

from webapp.models import Type, Status, Task, Project


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'name', 'description', 'users')
        read_only_fields = ('id', 'start_date', 'end_date')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')
        read_only_fields = ('id',)


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.PrimaryKeyRelatedField(read_only=True)
    type = TypeSerializer(read_only=True, many=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Task
        fields = (
            'id', 'summary', 'description', 'status', 'type', 'created_at', 'edit_time', 'is_deleted', 'project')
        read_only_fields = ('id', 'status', 'type', 'project', 'created_at', 'edit_time')


class StatusSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = Status
        fields = ('id', 'name', 'task')
        read_only_fields = ('id', 'task')
