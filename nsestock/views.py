from django.shortcuts import render
import requests
from nsetools import Nse
from .models import nsestock
from django.contrib import messages
from .nseform import nsestockform

app_name = "nsestock"

def nsehome(request):
    if request.method == 'POST':
        nsesearch = request.POST['nsesearch']
        nse = Nse()
        try:
            quote = nse.get_quote(nsesearch) 
        except Exception as e:
            quote = "Error..."
        return render(request, 'nsestock/nsehome.html', {'quote':quote})
    else:
        return render(request, 'nsestock/nsehome.html', {'nsesearch':'Enter the Indian Company symbol Above to search'})

def nseadd_stock(request):
    if request.method == 'POST':
       form = nsestockform(request.POST or None)
       if form.is_valid():
        form.save()
        messages.success(request, 'stock is been added')
        return render(request, 'nsestock/nseadd_stock.html')

    else:
        nsesearch = nsestock.objects.all()
        nse = Nse()
        nseoutput=[]
        for nsesearch_item in nsesearch:
            try:
                quote = nse.get_quote(str(nsesearch_item)) 
                nseoutput.append(quote)
            except Exception as e:
                quote = "Error..."
        return render(request, 'nsestock/nseadd_stock.html', {'nsesearch':nsesearch, 'nseoutput':nseoutput})


def nsedelete(request,nsestock_id):
    item = nsestock.objects.get(pk=nsestock_id)
    item.delete()
    messages.success(request, 'Stock has been deleted.')
    return render(request, 'nsestock/nseadd_stock.html')

def nsedelete_stock(request):
    nsesearch = nsestock.objects.all()
    return render(request, 'nsestock/nsedelete_stock.html',{'nsesearch':nsesearch})