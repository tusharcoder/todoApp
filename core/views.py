# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-09T22:35:30+05:30
# @Email:  tamyworld@gmail.com
# @Filename: views.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-12T22:28:22+05:30



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
    priority=serializers.IntegerField(required=False)
    def create(self, validated_data):
        """Method to create the comment"""
        from django.db.models import Max
        task=Task(**validated_data)
        try:
            task.priority=Task.objects.all().aggregate(Max('priority'))['priority__max']+1;
        except:
            task.priority=1;
        task.save()
        return task
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        target_priority=validated_data.get('priority',None)
        if not target_priority is None:
            try:
                task_with_given_priority = Task.objects.get(priority=target_priority)
            except Task.DoesNotExist:
                task_with_given_priority=None
            if not task_with_given_priority is None:
                """change the priority of the task"""
                task_with_given_priority.priority=instance.priority
                task_with_given_priority.save()
                instance.priority=target_priority
            else:
                """handle if no model found of the target priority"""
                relevent_task=self.getTargetPriorityTask(target_priority)
                if not relevent_task is None:
                    target_priority=relevent_task.priority
                    relevent_task.priority=instance.priority
                    relevent_task.save()
                    instance.priority=target_priority
                else:
                    instance.priority=1
        instance.save()
        return instance
    def getTargetPriorityTask(self,target_priority):
        """get the relevent target priority Task"""
        try:
            task=Task.objects.get(priority=target_priority)
        except Task.DoesNotExist:
            task=None
        if not task is None:
            return task
        else:
            if not target_priority is 1:
                return self.getTargetPriorityTask(target_priority-1)
            else:
                return None


class TaskList(APIView):
    """List all comments ur create new"""

    def get(self,request,format=None):
        tasks=Task.objects.order_by('priority')
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
        serializer = TaskSerializer(task)
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
