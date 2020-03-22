from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.utils import timezone
from .models import Todo
from django.http import Http404

# Create your views here.
todoList=[]
def index(request):
    # temp = {'id':1,"content":'a new todo task',"createtime":timezone.now()}
    # temp1 = {'id':2,"content":'a two todo task',"createtime":timezone.now()}
    todoList = Todo.objects.all()
    context={"data":todoList}
    return render(request,"index.html",context)
def add(request):
    '''
    :param request:
    :return: add a new todo and return index page
    '''
    if request.method == "GET":
        return render(request,'createTodo.html')
    elif request.method == "POST":
        todo_id =request.POST.get("todo_id")
        content = request.POST.get('content')
        createtime = request.POST.get('createtime')
        if todo_id and content and createtime:
            id = int(todo_id)
            ids = [int(todo.todo_id) for todo in Todo.objects.all()]
            print(ids)
            if id in ids:
                return render(request,'createTodo.html',{'error_message':"Todo任务已存在"})
            else:
                Todo.objects.create(todo_id=id,content=content,createtime=timezone.now())
                return redirect('/todo/list/')
        else:
            return render(request,"createTodo.html",{'error_message':"表单字段不能为空"})

def delete(request,todo_id):
    '''
    :param request:
    :param todo_id:
    :return: delete todo object according to todo_id and return index page
    '''
    try:
        Todo.objects.filter(todo_id=int(todo_id)).delete()
        return redirect('/todo/list/')

    except:
        return render(request,'index.html',{'message':'删除失败'})
def select(request,todo_id):
    '''
    :param request:
    :param todo_id:
    :return: 返回一个指定id的todo任务
    '''
    try:
        todo = Todo.objects.get(todo_id=int(todo_id))
    except Todo.DoesNotExist:
        raise Http404("Todo task {} does not exist".format(todo_id))
    context = {"data":todo}
    return render(request,"detail.html",context)

