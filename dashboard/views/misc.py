from django.shortcuts import render, redirect, get_object_or_404
from core.models.misc import Category, Animal
from dashboard.forms.misc import CategoryForm, AnimalForm
from dashboard.views.views1 import login_required_decorator


@login_required_decorator
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'dashboard/category/list.html', {'categories': categories})


@login_required_decorator
def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'dashboard/category/form.html', {'form': form})


@login_required_decorator
def category_update(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'dashboard/category/form.html', {'form': form})


@login_required_decorator
def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'dashboard/category/form.html', {'object': category})


# --- Animal Views ---
@login_required_decorator
def animal_list(request):
    animals = Animal.objects.all()
    return render(request, 'dashboard/animal/list.html', {'animals': animals})


@login_required_decorator
def animal_create(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm()
    return render(request, 'dashboard/animal/form.html', {'form': form})


@login_required_decorator
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            return redirect('animal_list')
    else:
        form = AnimalForm(instance=animal)
    return render(request, 'dashboard/animal/form.html', {'form': form})


@login_required_decorator
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    if request.method == 'POST':
        animal.delete()
        return redirect('animal_list')
    return render(request, 'dashboard/animal/form.html', {'object': animal})
