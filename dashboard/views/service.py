from django.shortcuts import render, redirect, get_object_or_404
from dashboard.views.views1 import login_required_decorator

from core.models.misc import Service, News
from dashboard.forms.misc import ServiceForm, NewsForm

@login_required_decorator

def service_list(request):
    services = Service.objects.all()
    return render(request, 'dashboard/service/list.html', {'services': services})

@login_required_decorator

def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm()
    return render(request, 'dashboard/service/form.html', {'form': form})

@login_required_decorator

def service_update(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('service_list')
    else:
        form = ServiceForm(instance=service)
    return render(request, 'dashboard/service/form.html', {'form': form})

@login_required_decorator

def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('service_list')
    return render(request, 'dashboard/service/form.html', {'object': service})


# --- News Views ---
@login_required_decorator

def news_list(request):
    news_list = News.objects.all()
    return render(request, 'dashboard/news/list.html', {'news_list': news_list})

@login_required_decorator

def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'dashboard/news/form.html', {'form': form})

@login_required_decorator

def news_update(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm(instance=news)
    return render(request, 'dashboard/news/form.html', {'form': form})

@login_required_decorator

def news_delete(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news.delete()
        return redirect('news_list')
    return render(request, 'dashboard/news/form.html', {'object': news})
