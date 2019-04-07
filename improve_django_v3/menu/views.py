from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import *
from .forms import *


def menu_list(request):
    menu = Menu.objects.all().prefetch_related('items')
    paginator = Paginator(menu, 5)

    page = request.GET.get('page')
    menus = paginator.get_page(page)
    return render(request, 'menu/list_all_current_menus.html',
                  {'menus': menus})


def menu_detail(request, pk):
    menu = Menu.objects.get(pk=pk)
    return render(request, 'menu/menu_detail.html', {'menu': menu})


def item_detail(request, pk):
    try:
        item = Item.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Http404
    return render(request, 'menu/detail_item.html', {'item': item})


def create_new_menu(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.created_date = timezone.now()
            menu.save()
            return redirect('menu:menu_detail', pk=menu.pk)
        else:
            messages.error(request, 'Please correct the error')
    else:
        form = MenuForm()
    return render(request, 'menu/menu_edit.html', {'form': form})


def edit_menu(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    form = MenuForm(instance=menu)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            return redirect('menu:menu_detail', pk=menu.pk)

    return render(request, 'menu/menu_edit.html', {
        'menu': menu,
        'form': form,
        })
