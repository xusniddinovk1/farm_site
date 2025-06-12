from django.shortcuts import redirect, get_object_or_404, render
from core.models.aboutUs import OurTeam
from dashboard.forms.aboutUs import OurTeamForm
from dashboard.views.views1 import login_required_decorator

@login_required_decorator

def ourteam_list(request):
    teams = OurTeam.objects.all()
    return render(request, 'dashboard/our_team/list.html', {'teams': teams})

@login_required_decorator

def ourteam_create(request):
    if request.method == 'POST':
        form = OurTeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ourteam_list')
    else:
        form = OurTeamForm()
    return render(request, 'dashboard/our_team/form.html', {'form': form})

@login_required_decorator

def ourteam_update(request, pk):
    team = get_object_or_404(OurTeam, pk=pk)
    if request.method == 'POST':
        form = OurTeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('ourteam_list')
    else:
        form = OurTeamForm(instance=team)
    return render(request, 'dashboard/our_team/form.html', {'form': form})

@login_required_decorator

def ourteam_delete(request, pk):
    team = get_object_or_404(OurTeam, pk=pk)
    if request.method == 'POST':
        team.delete()
        return redirect('ourteam_list')
    return render(request, 'dashboard/our_team/form.html', {'object': team})
