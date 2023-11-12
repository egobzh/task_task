from django.shortcuts import render,redirect
from django.views.generic.base import View
from datetime import date
#from.form import *

from .models import *

class index(View):
    def get(self, request):
        tasks = Tasks.objects.all()
        return render(request, 'index.html', {'tasks': tasks[::-1]})

class tasks(View):
    def post(self,request):
        name = request.POST['task']
        tasks = Tasks(name=name)
        tasks.save()
        return redirect('index')

class tasks_commit(View):
    def post(self,request,id):
        task = Tasks.objects.get(id=id)
        task.scheduled_date = date.today() if task.scheduled_date == None else None
        task.save()
        return redirect('index')
