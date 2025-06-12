from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator

from core.models.aboutUs import FarmHistory
from dashboard.forms.aboutUs import FarmHistoryForm

@login_required_decorator

def farmhistory_list(request):
    farmhistories = FarmHistory.objects.all()
    return render(request, 'dashboard/farm_history/list.html', {'farmhistories': farmhistories})

@login_required_decorator

def farmhistory_create(request):
    if request.method == 'POST':
        form = FarmHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farmhistory_list')
    else:
        form = FarmHistoryForm()
    return render(request, 'dashboard/farm_history/form.html', {'form': form})

@login_required_decorator

def farmhistory_update(request, pk):
    farmhistory = get_object_or_404(FarmHistory, pk=pk)
    if request.method == 'POST':
        form = FarmHistoryForm(request.POST, instance=farmhistory)
        if form.is_valid():
            form.save()
            return redirect('farmhistory_list')
    else:
        form = FarmHistoryForm(instance=farmhistory)
    return render(request, 'dashboard/farm_history/form.html', {'form': form})

@login_required_decorator

def farmhistory_delete(request, pk):
    farmhistory = get_object_or_404(FarmHistory, pk=pk)
    if request.method == 'POST':
        farmhistory.delete()
        return redirect('farmhistory_list')
    return render(request, 'dashboard/farm_history/form.html', {'object': farmhistory})
