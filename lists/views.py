from django.shortcuts import render
from list.models import Item

def add_item(request):
    if request.method == 'POST' and request.POST['item_name']:
        Item.objects.create(name=request.POST['item_name'], 
