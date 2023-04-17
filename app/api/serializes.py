from rest_framework import serializers
from .models import Task, Project, Status, Type


class TaskSerializer(serializers.ModelSerializer):
    class TaskSerializer(serializers.ModelSerializer):
        status = serializers.PrimaryKeyRelatedField(many=True, queryset=Status.objects.all(), read_only=True)
        type = serializers.PrimaryKeyRelatedField(many=True, queryset=Type.objects.all(), read_only=True)

        class Meta:
            model = Task
            fields = (
                'id', 'summary', 'description', 'status', 'type', 'created_at', 'edit_time', 'is_deleted', 'project')
            read_only_fields = ('id', 'is_deleted')


class ProjectSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'name', 'description', 'users')
        read_only_fields = ('id', 'start_date', 'end_date')


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')
        read_only_fields = ('id',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')
        read_only_fields = ('id',)
