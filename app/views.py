from django.shortcuts import render
from .models import Task
from django.utils.timezone import now
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import TaskForm
from django.shortcuts import redirect


@login_required
def dashboard(request):

    tasks = Task.objects.all()

    total_tasks = tasks.count()

    completed_tasks = tasks.filter(
        status='Completed'
    ).count()

    pending_tasks = tasks.filter(
        status='Pending'
    ).count()

    overdue_tasks = tasks.filter(
        due_date__lt=now().date()
    ).count()

    
    if request.method == 'POST':

        form = TaskForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/')

    else:
        form = TaskForm()
    context = {
        'tasks': tasks,
        'total_tasks': total_tasks,
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'overdue_tasks': overdue_tasks,
        'form':form,
    }

    return render(request, 'dashboard.html', context)

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProjectSerializer, TaskSerializer
from .models import Project


@api_view(['GET'])
def project_api(request):

    projects = Project.objects.all()
    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def task_api(request):

    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(
        assigned_to=request.user
        )
    serializer = TaskSerializer(tasks, many=True)

    return Response(serializer.data)

class CustomLoginView(LoginView):
    template_name='login.html'