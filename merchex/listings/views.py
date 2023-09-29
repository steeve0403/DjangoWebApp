from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import redirect
from django.core.mail import send_mail

from listings.models import Band
from listings.forms import BandForm, ContactUsForm




def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'listings/band_list.html',
                  {'bands': bands})

def band_detail(request, id):
    band = Band.objects.get(id=id)
    return render(request,
                  'listings/band_detail.html',
                  {'band': band})

def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'listings/band_create.html',
                  {'form': form})


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1> <p>Faites votre choix</p>')

def contact(request):

    if request.method =='POST':
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme" } via MerchEx Contact Us Form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return  redirect('email-sent')
    else:
        form = ContactUsForm()

    return render(request,
                  'listings/contact.html',
                  { 'form':form })

    print('La méthode de requête est : ', request.method)
    print('Les données POST sont :', request.POST)

    form = ContactUsForm()

