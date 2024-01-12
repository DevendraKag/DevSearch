from django.urls import path
from .views import project, projects


urlpatterns = [
    path('', project, name='projects'),
    path('project/<str:pk>', projects, name='project')
]
