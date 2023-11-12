from django.urls import path
from . import views

urlpatterns = [path('', views.index.as_view(),name='index'), path('task_add',views.tasks.as_view()),path('tasks_commit/<int:id>',views.tasks_commit.as_view()),]