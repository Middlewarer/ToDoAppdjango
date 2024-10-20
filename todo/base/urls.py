from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from debug_toolbar.toolbar import debug_toolbar_urls

app_name = 'base'

urlpatterns = [
    path('', views.DefaultPage.as_view(), name='default_page'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', views.TaskDelete.as_view(), name='task_delete'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='base:login'), name='logout'),
    path('register/', views.RegisterPage.as_view(), name='register'),
    path('task/<int:pk>/complete', views.complete_task, name='complete_task'),
]