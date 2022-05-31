from django.shortcuts import render, redirect
from . models import Task

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer


def home(request):
    # value = student.objects.all()
    # context = {
    #     'dataname': value
    # }
    return render(request,'index.html')
# def data(request):
#     a = request.POST.get('name')
#     b = request.POST.get('age')
#     student.objects.create(name=a,age=b)
#     value = student.objects.all()
#     context = {
#         'dataname': value
#     }
#     return render(request,'index.html',context)
# def deletefunction(request,pk):
#     data=student.objects.get(id=pk)
#     data.delete()
#     value = student.objects.all()
#     context = {
#         'dataname': value
#     }
#     return render(request,'index.html',context)
# def updatefunction(request,pk):
#     data = student.objects.get(id=pk)
#     if request.method=='POST':
#         name = request.POST.get('name')
#         age = request.POST.get('age')
#         student.objects.filter(id=pk).update(name=name,age=age)
#
#         return redirect(home)
#     context = {
#         'dataname': data
#     }
#
#     return render(request,'edit.html',context)

@api_view(['GET','POST'])
def apiOverview(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
	tasks = Task.objects.get(id=pk)
	serializer = TaskSerializer(tasks, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
	serializer = TaskSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
	task = Task.objects.get(id=pk)
	serializer = TaskSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def taskDelete(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

