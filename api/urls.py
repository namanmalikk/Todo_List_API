from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="apiOverview"),
    path('list/', views.taskList, name="taskList"),
    path('create/', views.taskCreate, name="taskCreate"),

    path('detail/<int:pk>/', views.taskDetail, name="taskDetail"),
    path('update/<int:pk>/', views.taskUpdate, name="taskUpdate"),
    path('delete/<int:pk>/', views.taskDelete, name="taskDelete"),
]
