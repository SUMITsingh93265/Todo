from django.shortcuts import render, redirect
from home.models import *
# Create your views here.


def index(request):
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')

        Todo.objects.create(
            title=title,
            description=description,
        )
        return redirect('/index')

    queryset = Todo.objects.all()
    context = {'index': queryset}

    return render(request, "index.html", context)


def update(request, id):
    queryset = Todo.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        title = data.get('title')
        description = data.get('description')

        queryset.title = title
        queryset.description = description

        queryset.save()
        return redirect('/index/')

    context = {'item': queryset}

    return render(request, 'update.html', context)


def delete(request, id):
    queryset = Todo.objects.get(id=id)
    queryset.delete()
    return redirect('/index')