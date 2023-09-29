from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from  listings.forms import ContactUsForm


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  { 'bands':bands })

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Faites votre choix</p>')

def contact(request):
    form = ContactUsForm()
    return render(request,
                  'listings/contact.html',
                  { 'form':form })

