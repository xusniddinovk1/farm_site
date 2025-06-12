from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator
from core.models.product2 import Work
from core.models.product3 import Aminoacid, Food
from dashboard.forms.product2 import WorkForm
from dashboard.forms.product3 import AminoacidForm, FoodForm


@login_required_decorator
def work_list(request):
    paints = Work.objects.all()
    return render(request, 'dashboard/work/list.html', {'paints': paints})


@login_required_decorator
def work_create(request):
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('work_list')
    else:
        form = WorkForm()
    return render(request, 'dashboard/work/form.html', {'form': form})


@login_required_decorator
def work_update(request, pk):
    paint = get_object_or_404(Work, pk=pk)
    if request.method == 'POST':
        form = WorkForm(request.POST, request.FILES, instance=paint)
        if form.is_valid():
            form.save()
            return redirect('work_list')
    else:
        form = WorkForm(instance=paint)
    return render(request, 'dashboard/work/form.html', {'form': form})


@login_required_decorator
def work_delete(request, pk):
    work = get_object_or_404(Work, pk=pk)
    work.delete()
    return redirect('work_list')


@login_required_decorator
def aminoacids_list(request):
    aminoacids = Aminoacid.objects.all()
    return render(request, 'dashboard/aminoacid/list.html', {'aminoacids': aminoacids})


@login_required_decorator
def aminoacids_create(request):
    if request.method == 'POST':
        form = AminoacidForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('aminoacids_list')
    else:
        form = AminoacidForm()
    return render(request, 'dashboard/aminoacid/form.html', {'form': form})


@login_required_decorator
def aminoacids_update(request, pk):
    paint = get_object_or_404(Aminoacid, pk=pk)
    if request.method == 'POST':
        form = AminoacidForm(request.POST, request.FILES, instance=paint)
        if form.is_valid():
            form.save()
            return redirect('aminoacids_list')
    else:
        form = AminoacidForm(instance=paint)
    return render(request, 'dashboard/aminoacid/form.html', {'form': form})


@login_required_decorator
def aminoacids_delete(request, pk):
    aminoacid = get_object_or_404(Aminoacid, pk=pk)
    aminoacid.delete()
    return redirect('aminoacids_list')


@login_required_decorator
def food_list(request):
    foods = Food.objects.all()
    return render(request, 'dashboard/food/list.html', {'foods': foods})


@login_required_decorator
def food_create(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'dashboard/food/form.html', {'form': form})


@login_required_decorator
def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'dashboard/food/form.html', {'form': form})


@login_required_decorator
def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    food.delete()
    return redirect('food_list')
