from django.shortcuts import render, get_object_or_404, redirect
from dashboard.views.views1 import login_required_decorator
from core.models.product2 import Equipment, Paint
from dashboard.forms.product2 import EquipmentForm, PaintForm


@login_required_decorator
def equipments_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'dashboard/equipment/list.html', {'equipments': equipments})


@login_required_decorator
def equipment_create(request):
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('equipments_list')
    else:
        form = EquipmentForm()
    return render(request, 'dashboard/equipment/form.html', {'form': form})


@login_required_decorator
def equipment_update(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        form = EquipmentForm(request.POST, request.FILES, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipments_list')
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'dashboard/equipment/form.html', {'form': form})


@login_required_decorator
def equipments_delete(request, pk):
    equipment = get_object_or_404(Equipment, pk=pk)
    equipment.delete()
    return redirect('vitaminsminerals_list')


# --- Paint Views ---
@login_required_decorator
def paints_list(request):
    paints = Paint.objects.all()
    return render(request, 'dashboard/paint/list.html', {'paints': paints})


@login_required_decorator
def paint_create(request):
    if request.method == 'POST':
        form = PaintForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('paints_list')
    else:
        form = PaintForm()
    return render(request, 'dashboard/paint/form.html', {'form': form})


@login_required_decorator
def paint_update(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    if request.method == 'POST':
        form = PaintForm(request.POST, request.FILES, instance=paint)
        if form.is_valid():
            form.save()
            return redirect('equipments_list')
    else:
        form = PaintForm(instance=paint)
    return render(request, 'dashboard/paint/form.html', {'form': form})


@login_required_decorator
def paint_delete(request, pk):
    paint = get_object_or_404(Paint, pk=pk)
    paint.delete()
    return redirect('paints_list')
