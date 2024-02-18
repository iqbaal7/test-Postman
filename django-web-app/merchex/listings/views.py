from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Band
from django.core.mail import send_mail
from listings.forms import BandForm, ContactUsForm
from django.shortcuts import redirect


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request, 'listings/band_create.html', {'form': form})

def contact(request):
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect("email-envoye")
    else:
        # Ceci doit être une requête GET, donc créer un formulaire vide
        form = ContactUsForm()

    return render(request, 'listings/contact.html', {'form': form})


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