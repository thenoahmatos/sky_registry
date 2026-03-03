from django.shortcuts import render, get_object_or_404
from .models import Team

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams})

def team_detail(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    return render(request, 'teams/team_detail.html', {'team': team})


def team_create(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        department = request.POST.get("department", "")
        manager = request.POST.get("manager", "")
        description = request.POST.get("description", "")

        Team.objects.create(
            name=name,
            department=department,
            manager=manager,
            description=description,
        )

        teams = Team.objects.all()
        return render(request, 'teams/team_list.html', {'teams': teams})

    return render(request, 'teams/team_create.html')

