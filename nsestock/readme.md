django version 4.1
python version 3.8
step.1: 1st we created new app using app startapp nsestock

step.2: created urls.py and added url than in views.py defining function nsehome 

step.3: tested it

step.4: in templates created home.html and base.html

step.5: added pipelines

step.6: in views.py imported
from django.shortcuts import render
import requests
from nsetools import Nse

and defined def nsehome

step.7:  tested function to display output in html using {{quote}}

step.8: adding search functionality by targeting search with name = nse_search

step.9: using for loop and if statement in html showing data


created an add_stock and added pipeline

step.10 now created database by adding class in model

step.11: once created imported to admin site so that it is visible there

step.12: than that class from models file imported to views.py 
from .models import nsestock
and by using nsestock.objects.all() : command fetching all data

and showing data in nse_stock page..

step.13: to add stock using button and than adding to database we imported
form django.contrib import messages
from .forms import nsestock form

than added conditions in views.py

step.14 creating forms.py in that creating class nsestockform 
imports
from django import forms
from .models import nsestock



delete stock in database..


step.15: defined a fuunction nse delete
targeting id by using objects.get(pk=nsestock_id)
item.delete()
and created one link by using anchor tag. to delete


Cleaning data by adding it in Table format

step.16: added table from bootsrap

step.17: usin


step.15:


step.15:

step.15:

