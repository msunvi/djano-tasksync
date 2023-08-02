from django.shortcuts import render
from django.http.response import HttpResponse
from todo.models import TodoItem, User
from django.db.models import Q, F
from django.db import connection


def sayHello(request):
    # todos = User.objects.filter(email__contains='.net')
    # todos = TodoItem.objects.filter(Q(id__lt=10) & ~Q(user__email__contains=".com")).order_by('-title', 'id')
    todos = TodoItem.objects.values('id', 'title', 'user__email')[5:10]
    return render(request, 'hello.html', {'name': "Sunvi", 'todos': list(todos)})
