from django.urls import path
from .views import RegisterUserView, CustomTokenObtainPairView, UserDetailView,ProjectListView, ProjectDetailView, TaskListCreateView, TaskDetailView, CommentListCreateView, CommentDetailView

urlpatterns = [
    path('api/users/register/', RegisterUserView.as_view(), name='register'),
    path('api/users/login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),


    
    path('api/projects/', ProjectListView.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),

    path('api/projects/<int:project_id>/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),

    
 
    path('api/tasks/<int:task_id>/comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('api/comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
