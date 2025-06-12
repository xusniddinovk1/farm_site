from django.shortcuts import render, redirect, get_object_or_404
from dashboard.forms.aboutUs import *
from dashboard.views.views1 import login_required_decorator


@login_required_decorator
def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'dashboard/partner/list.html', {'partners': partners})


@login_required_decorator
def partner_create(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm()
    return render(request, 'dashboard/partner/form.html', {'form': form})


@login_required_decorator
def partner_update(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partner_list')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'dashboard/partner/form.html', {'form': form})


@login_required_decorator
def partner_delete(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    partner.delete()
    return redirect('partner_list')


@login_required_decorator
def partner_image_list(request):
    partner_images = PartnerImage.objects.all()
    return render(request, 'dashboard/partner_image/list.html', {'partner_images': partner_images})


@login_required_decorator
def partner_image_create(request):
    if request.method == 'POST':
        form = PartnerImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partner_image_list')
    else:
        form = PartnerImageForm()
    return render(request, 'dashboard/partner_image/form.html', {'form': form})


@login_required_decorator
def partner_image_update(request, pk):
    partner_image = get_object_or_404(PartnerImage, pk=pk)
    if request.method == 'POST':
        form = PartnerImageForm(request.POST, request.FILES, instance=partner_image)
        if form.is_valid():
            form.save()
            return redirect('partner_image_list')
    else:
        form = PartnerImageForm(instance=partner_image)
    return render(request, 'dashboard/partner_image/form.html', {'form': form})


@login_required_decorator
def partner_image_delete(request, pk):
    partner_image = get_object_or_404(PartnerImage, pk=pk)
    partner_image.delete()
    return redirect('partner_image_list')
