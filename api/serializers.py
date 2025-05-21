from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User

MIN_LENGTH=8
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        write_only=True,
        min_legth=MIN_LENGTH
    )

    class Meta:
        model = User