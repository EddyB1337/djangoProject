from django.shortcuts import render, get_object_or_404
from .models import Produkt


# Create your views here.
def detail(request, pk):
    item = get_object_or_404(Produkt, pk=pk)
    related_items = Produkt.objects.filter(category=item.category).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })
