from django.shortcuts import render, get_object_or_404

from item.models import Kategorie, Produkt


# Create your views here.

def index(request):
    items = Produkt.objects.all()[0:6]
    categories = Kategorie.objects.all()
    return render(request, "personal/index.html", {
        'categories': categories,
        'items': items,
    })


def categoryIndex(request, pk):
    categories = Kategorie.objects.all()
    category = get_object_or_404(Kategorie, pk=pk)
    related_items_to_category = Produkt.objects.filter(category=category).exclude(pk=pk)
    return render(request, "personal/categoryIndex.html", {
        'category': category,
        'related_items_to_category': related_items_to_category,
        'categories': categories,
    })


def contact(request):
    return render(request, "personal/contact.html")
