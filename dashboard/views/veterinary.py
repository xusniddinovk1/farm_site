from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator
from core.models.product import VeterinaryDrugs, Vaccine
from dashboard.forms.product import VeterinaryDrugsForm, VaccineForm

@login_required_decorator

def veterinarydrugs_list(request):
    drugs = VeterinaryDrugs.objects.all()
    return render(request, 'dashboard/veterinary/list.html', {'drugs': drugs})

@login_required_decorator

def veterinarydrugs_create(request):
    if request.method == 'POST':
        form = VeterinaryDrugsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('veterinarydrugs_list')
    else:
        form = VeterinaryDrugsForm()
    return render(request, 'dashboard/veterinary/form.html', {'form': form})

@login_required_decorator

def veterinarydrugs_update(request, pk):
    drug = get_object_or_404(VeterinaryDrugs, pk=pk)
    if request.method == 'POST':
        form = VeterinaryDrugsForm(request.POST, request.FILES, instance=drug)
        if form.is_valid():
            form.save()
            return redirect('veterinarydrugs_list')
    else:
        form = VeterinaryDrugsForm(instance=drug)
    return render(request, 'dashboard/veterinary/form.html', {'form': form})

@login_required_decorator

def veterinarydrugs_delete(request, pk):
    drug = get_object_or_404(VeterinaryDrugs, pk=pk)
    if request.method == 'POST':
        drug.delete()
        return redirect('veterinarydrugs_list')
    return render(request, 'dashboard/veterinary/form.html', {'object': drug})


# --- Vaccine Views ---
@login_required_decorator

def vaccine_list(request):
    vaccines = Vaccine.objects.all()
    return render(request, 'dashboard/vaccine/list.html', {'vaccines': vaccines})

@login_required_decorator

def vaccine_create(request):
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vaccine_list')
    else:
        form = VaccineForm()
    return render(request, 'dashboard/vaccine/form.html', {'form': form})

@login_required_decorator

def vaccine_update(request, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES, instance=vaccine)
        if form.is_valid():
            form.save()
            return redirect('vaccine_list')
    else:
        form = VaccineForm(instance=vaccine)
    return render(request, 'dashboard/vaccine/form.html', {'form': form})

@login_required_decorator

def vaccine_delete(request, pk):
    vaccine = get_object_or_404(Vaccine, pk=pk)
    if request.method == 'POST':
        vaccine.delete()
        return redirect('vaccine_list')
    return render(request, 'dashboard/vaccine/form.html', {'object': vaccine})
