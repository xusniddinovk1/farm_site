from django.shortcuts import render, get_object_or_404, redirect

from core.models.aboutUs import AboutUs
from dashboard.forms.aboutUs import AboutUsForm
from dashboard.views.views1 import login_required_decorator


@login_required_decorator
def about_us_list(request):
    abouts = AboutUs.objects.all()
    return render(request, 'dashboard/aboutUs/list.html', {'abouts': abouts})


@login_required_decorator
def about_us_create(request):
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('about_us_list')
    else:
        form = AboutUsForm()
    return render(request, 'dashboard/aboutUs/form.html', {'form': form})


@login_required_decorator
def about_us_update(request, pk):
    about = get_object_or_404(AboutUs, pk=pk)
    if request.method == 'POST':
        form = AboutUsForm(request.POST, request.FILES, instance=about)
        if form.is_valid():
            form.save()
            return redirect('about_us_list')
    else:
        form = AboutUsForm(instance=about)
    return render(request, 'dashboard/aboutUs/form.html', {'form': form})


@login_required_decorator
def about_us_delete(request, pk):
    about = get_object_or_404(AboutUs, pk=pk)
    about.delete()
    return redirect('about_us_list')
