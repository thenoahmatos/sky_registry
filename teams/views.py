from django.shortcuts import render, get_object_or_404, redirect
from .models import Team

from django.db.models import Q

def team_list(request):
    query = request.GET.get('q')

    if query:
        teams = Team.objects.filter(
    Q(name__icontains=query) |
    Q(department__icontains=query) |
    Q(manager__icontains=query)
)
    else:
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

        return redirect('team_list')

    return render(request, 'teams/team_create.html')


def team_edit(request, team_id):
    team = get_object_or_404(Team, id=team_id)

    if request.method == "POST":
        team.name = request.POST.get('name')
        team.department = request.POST.get('department')
        team.manager = request.POST.get('manager')
        team.save()
        return redirect('team_list')

    return render(request, 'teams/team_form.html', {'team': team})

def team_delete(request, team_id):
    team = get_object_or_404(Team, id=team_id)
    team.delete()
    return redirect('team_list')

