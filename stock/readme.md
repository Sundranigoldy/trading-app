created an trading app using startproject command
created stocks app in that using startapp command
added pipeline betn
urls.py (traingapp) ----> urls.py(stocks) ----> (views) ---> (html template)


imported json for making human readable

imported requests to handle api

api taken from base of website iex cloud  https://cloud.iexapis.com
/stable/stock/aapl/quote? ---> to get an statble version of stock of apple/ we are taking quote
than token generated..

once we got an stock data 
we used oops concepts to show data which necesaary important for us using dot method..

working on search and form for now..
1st gives action as / 
than scrf token
than name = search
so that we can access it in views.py
where we added if statement for post method in name search

than we call api which is an json file and we parse with json.loads
else error..

if search is correct than it gives that apps name and other variable which we have passed in home.html

made an add_stock.html

created an database in models for company name and price
than push to databse using make migrations and migrate

we can check using admin page.
for that we need to create superuser

now to pulll stuff from database we use
objects.all() command in add stock and add in an variable and pass in add stock.html

in views.py we added using import statment

from django.shortcuts import redirect
from django.contrib import messages
from .form import stockForm (while this one is yet to be created..)

in form.py we import

from django import forms
from .models import stock

