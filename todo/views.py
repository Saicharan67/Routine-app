from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from .models import Todo
# Create your views here.
def index(request):
    todo_list = Todo.objects.order_by('id')
    context = {'todo_list' : todo_list}
    return render(request,'todo/index.html',context)

@require_POST
def addTodo(request):
    form = request.POST['inputtodo']
    if len(form)<50 and len(form)!=0:
        new_todo = Todo(text=request.POST['inputtodo'])
        new_todo.save()
    
    return redirect('index')
def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()

    return redirect('index')

def delcompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')
def delall(request):
    Todo.objects.all().delete()

    return redirect('index')