from django.shortcuts import render
from app.models import Todo
def home(request):
    completed_task = Todo.objects.filter(is_completed=True)
    uncompleted_task = Todo.objects.filter(is_completed=False)
    context={
       'completed_task':completed_task,
       'uncompleted_task':uncompleted_task,
    }
    return render(request,'index.html',context)