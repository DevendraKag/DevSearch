from django.shortcuts import render


projectList = [
    {
        "id": '1',
        "name": "E-commerce",
        "description": "This projects is for Ecommerce platform"
    },
    {
        "id": '2',
        "name": "Electronic",
        "description": "This projects is for Electronic products"
    },
    {
        "id": '3',
        "name": "Consumer Goods",
        "description": "This projects is for Consumer Goods"
    }
]


def projects(request, pk):
    projectObj = None
    for i in projectList:
        if i['id'] == pk:
            projectObj = i
    # return HttpResponse(f"This if response of projects {pk}")
    return render(request, 'projects/projects.html', {'projectobj': projectObj})


def project(request):
    number = 9
    page = "Projects"
    context = {"page": page, 'number': number, 'projects': projectList}
    # return HttpResponse("This is my response")
    return render(request, 'projects/single-project.html', context)
