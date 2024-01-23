from django.shortcuts import render
from .models import Project, Tag


def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    # return HttpResponse(f"This if response of projects {pk}")
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    project_obj = Project.objects.get(id=pk)
    tags = Tag.objects.all()
    context = {"project": project_obj, 'tags': tags}
    # return HttpResponse("This is my response")
    return render(request, 'projects/single-project.html', context)
