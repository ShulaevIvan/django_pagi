import csv
from pprint import pprint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator




def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    
    
    with open('data-398-2018-08-30.csv', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        content = []
        for line in reader:
            station = {}
            station['Name'] = line['Name']
            station['Street'] = line['Street']
            station['District'] = line['District']
            content.append(station)
    
        
        
        paginator = Paginator(content, 10)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        
        context = {
           'page': page,
           'bus_stations': content,
        }

        return render(request, 'stations/index.html', context)
