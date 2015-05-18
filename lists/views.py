from django.shortcuts import render, render_to_response
from lists.models import Item
from django import forms


class ImageUploadForm(forms.Form):
    item_name = forms.CharField(max_length = 50)
    image_file = forms.ImageField()


def add_item(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
        #Item.objects.create(name=request.POST['item_name'], 
        #        image=request.POST['image'])
        Item.objects.create(name=request.POST.get('item_name'),
                           image = request.POST.get('image', False))
            #return HttpResponseRedirect('/lists/add_item.html')
    #return render(request, 'lists/add_item.html')
    return render(request, 'lists/upload.html', {'form': form})


def show_add_page(request):
    #return render_to_response('lists/add_item.html')
    return render(request, 'lists/add_item.html')
            
