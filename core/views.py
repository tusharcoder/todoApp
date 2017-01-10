# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-09T22:35:30+05:30
# @Email:  tamyworld@gmail.com
# @Filename: views.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-10T13:15:51+05:30



from django.shortcuts import render
from .models import Task
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
# Create your views here.

#serializers
class TaskSerializer(serializers.Serializer):
    """serializer of the comment"""
    id=serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=500)
    def create(self, validated_data):
        """Method to create the comment"""
        task=Task(**validated_data)
        task.save()
        return task
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class TaskList(APIView):
    """List all comments ur create new"""

    def get(self,request,format=None):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(APIView):
    """Detail view for the comment"""
    def get_object(self, pk):
        try:
            return Task.objects.get(pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        task = self.get_object(pk)
        serializer = TaskSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        task=self.get_object(pk)
        serializer=TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
