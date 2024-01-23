from django.urls import path
from .views import project, projects


urlpatterns = [
    path('project/<str:pk>', project, name='project'),
    path('projects/', projects, name='projects')
]
