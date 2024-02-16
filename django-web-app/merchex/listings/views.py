from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
# Create your views here.

from listings.forms import ContactUsForm

def contact(request):
  form = ContactUsForm()  # ajout d’un nouveau formulaire ici
  return render(request,
          'listings/contact.html',
          {'form': form})

def hello(request):
    bands = Band.objects.all()
    return render(request, 'listings\hello.html',
                  context={"bands": bands})

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})

def band_detail(request, id):
  band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) # nous mettons à jour cette ligne pour passer le groupe au gabarit

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')