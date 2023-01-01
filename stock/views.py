from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
import json
from .models import stock
from django.contrib import messages
from .form import stockform
app_name = "stock"
# Create your views here.
def home(request):
    if request.method == "POST":
        search = request.POST['search']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ search + "/quote?token=pk_92e5de89fc324df881645ad170980dc7")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error.."

        return render(request,"stock/home.html", {'api':api})

    else:
        return render(request,"stock/home.html", {'search':"Enter the company to search"})
def add_stock(request):
    if request.method == "POST":
        form = stockform(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, ('You stock has been added'))
            return render(request, 'stock/add_stock.html')
    else:
        search = stock.objects.all()
        output =[]
        for search_item in search:
            api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ str(search_item) + "/quote?token=pk_92e5de89fc324df881645ad170980dc7")
            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error.."

        return render(request, 'stock/add_stock.html', {'search': search, 'output':output})

def delete(request,stock_id):
    item = stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ('Stock has been deleted'))
    return render (request, 'stock/delete_stock.html')

def delete_stock(request):
    search = stock.objects.all()
    return render(request, 'stock/delete_stock.html', {'search': search})