from django.shortcuts import render, redirect, get_object_or_404
from core.models.aboutUs import Manufacturing
from dashboard.forms.aboutUs import ManufacturingForm
from dashboard.views.views1 import login_required_decorator

@login_required_decorator

def manufacturing_list(request):
    manufacturings = Manufacturing.objects.all()
    return render(request, 'dashboard/manufacturing/list.html', {'manufacturings': manufacturings})

@login_required_decorator

def manufacturing_create(request):
    if request.method == 'POST':
        form = ManufacturingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('manufacturing_list')
    else:
        form = ManufacturingForm()
    return render(request, 'dashboard/manufacturing/form.html', {'form': form})

@login_required_decorator

def manufacturing_update(request, pk):
    manufacturing = get_object_or_404(Manufacturing, pk=pk)
    if request.method == 'POST':
        form = ManufacturingForm(request.POST, request.FILES, instance=manufacturing)
        if form.is_valid():
            form.save()
            return redirect('manufacturing_list')
    else:
        form = ManufacturingForm(instance=manufacturing)
    return render(request, 'dashboard/manufacturing/form.html', {'form': form})

@login_required_decorator

def manufacturing_delete(request, pk):
    manufacturing = get_object_or_404(Manufacturing, pk=pk)
    if request.method == 'POST':
        manufacturing.delete()
        return redirect('manufacturing_list')
    return render(request, 'dashboard/manufacturing/form.html', {'object': manufacturing})
