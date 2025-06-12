from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator
from core.models.aboutUs import FarmHistory
from dashboard.forms.aboutUs import FarmHistoryForm


@login_required_decorator
def farm_history_list(request):
    farm_histories = FarmHistory.objects.all()
    return render(request, 'dashboard/farm_history/list.html', {'farm_histories': farm_histories})


@login_required_decorator
def farm_history_create(request):
    if request.method == 'POST':
        form = FarmHistoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('farm_history_list')
    else:
        form = FarmHistoryForm()
    return render(request, 'dashboard/farm_history/form.html', {'form': form})


@login_required_decorator
def farm_history_update(request, pk):
    farm_history = get_object_or_404(FarmHistory, pk=pk)
    if request.method == 'POST':
        form = FarmHistoryForm(request.POST, instance=farm_history)
        if form.is_valid():
            form.save()
            return redirect('farm_history_list')
    else:
        form = FarmHistoryForm(instance=farm_history)
    return render(request, 'dashboard/farm_history/form.html', {'form': form})


@login_required_decorator
def farm_history_delete(request, pk):
    farm_history = get_object_or_404(FarmHistory, pk=pk)
    farm_history.delete()
    return redirect('farm_history_list')
