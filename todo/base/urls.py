from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'base'

urlpatterns = [
    path('', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/create/', views.TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout')
]