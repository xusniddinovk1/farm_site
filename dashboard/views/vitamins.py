from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator

from core.models.product1 import CleaningProducts, VitaminsMinerals
from dashboard.forms.product1 import CleaningProductsForm, VitaminsMineralsForm


@login_required_decorator
def cleaningproducts_list(request):
    cleaning_products = CleaningProducts.objects.all()
    return render(request, 'dashboard/cleaning/list.html', {'cleaning_products': cleaning_products})


@login_required_decorator
def cleaningproducts_create(request):
    if request.method == 'POST':
        form = CleaningProductsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('cleaningproducts_list')
    else:
        form = CleaningProductsForm()
    return render(request, 'dashboard/cleaning/form.html', {'form': form})


@login_required_decorator
def cleaningproducts_update(request, pk):
    cleaning_product = get_object_or_404(CleaningProducts, pk=pk)
    if request.method == 'POST':
        form = CleaningProductsForm(request.POST, request.FILES, instance=cleaning_product)
        if form.is_valid():
            form.save()
            return redirect('cleaningproducts_list')
    else:
        form = CleaningProductsForm(instance=cleaning_product)
    return render(request, 'dashboard/cleaning/form.html', {'form': form})


@login_required_decorator
def cleaningproducts_delete(request, pk):
    cleaning_product = get_object_or_404(CleaningProducts, pk=pk)
    if request.method == 'POST':
        cleaning_product.delete()
        return redirect('cleaningproducts_list')
    return render(request, 'dashboard/cleaning/form.html', {'object': cleaning_product})


# --- VitaminsMinerals Views ---
@login_required_decorator
def vitaminsminerals_list(request):
    vitaminsminerals = VitaminsMinerals.objects.all()
    return render(request, 'dashboard/vitamins/list.html', {'vitaminsminerals': vitaminsminerals})


@login_required_decorator
def vitaminsminerals_create(request):
    if request.method == 'POST':
        form = VitaminsMineralsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vitaminsminerals_list')
    else:
        form = VitaminsMineralsForm()
    return render(request, 'dashboard/vitamins/form.html', {'form': form})


@login_required_decorator
def vitaminsminerals_update(request, pk):
    vitamin = get_object_or_404(VitaminsMinerals, pk=pk)
    if request.method == 'POST':
        form = VitaminsMineralsForm(request.POST, request.FILES, instance=vitamin)
        if form.is_valid():
            form.save()
            return redirect('vitaminsminerals_list')
    else:
        form = VitaminsMineralsForm(instance=vitamin)
    return render(request, 'dashboard/vitamins/form.html', {'form': form})


@login_required_decorator
def vitaminsminerals_delete(request, pk):
    vitamin = get_object_or_404(VitaminsMinerals, pk=pk)
    if request.method == 'POST':
        vitamin.delete()
        return redirect('vitaminsminerals_list')
    return render(request, 'dashboard/vitamins/form.html', {'object': vitamin})
