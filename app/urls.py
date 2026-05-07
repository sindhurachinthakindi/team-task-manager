from django.urls import path
from .views import dashboard, project_api, task_api, CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', CustomLoginView.as_view(), name='login'),

    path('logout/', LogoutView.as_view()),

    path('', dashboard, name='dashboard'),

    path('api/projects/', project_api),

    path('api/tasks/', task_api),
]