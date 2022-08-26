from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *

from datetime import date

# Create your views here.
def mostrar_familiares(request):

    data = {'lista_familiares': [{'nombre': 'Angel Andre', 'apellido': 'Carreon Juarez', 'parentesco': 'Hijo', 'edad': 2.5, 'date_of_birdth': date(2020, 2, 21)},
                                 {'nombre': 'Claudia', 'apellido': 'Juarez Velazquez', 'parentesco': 'Esposa', 'edad': 32, 'date_of_birdth': date(1990, 2, 8)},
                                 {'nombre': 'Jose Luis', 'apellido': 'Carreon Flores', 'parentesco': 'Padre', 'edad': 62, 'date_of_birdth': date(1959, 6, 21)},
                                 {'nombre': 'Bernardo', 'apellido': 'Carreon Hernandez', 'parentesco': 'Abuelo', 'edad': 93, 'date_of_birdth': date(1929, 8, 20)},
                                 {'nombre': 'Victor Hugo', 'apellido': 'Carreon Silva', 'parentesco': 'Hermano', 'edad': 23, 'date_of_birdth': date(1999, 3, 2)},
                                 ]}

    for familiar in data['lista_familiares']:
        pariente = Familiar(nombre=familiar['nombre'],
                            apellido=familiar['apellido'],
                            parentesco=familiar['parentesco'],
                            edad=familiar['edad'],
                            date_of_birdth=familiar['date_of_birdth'])
        pariente.save()

    #load template
    my_template = loader.get_template('template1.html')

    #render the context
    document = my_template.render(data)

    return HttpResponse(document)