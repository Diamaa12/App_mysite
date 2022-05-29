import logging

from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from webapp.user_class.users import Users
from django.contrib import messages

import typer
# Create your views here.
def index_webapp(requete):
    user = Users(name="Mamadou", username="Diallo", age=3, message="Longue vie à toi.")
    #print(f"Utilisateur enregitstrer{user.recup_data()}")
    data = user.recup_data()
    return render(requete, 'forum.html', {"users":data})
def add_contact(request):
    name = request.POST.get("Name")
    user_name = request.POST.get("username")
    age = request.POST.get("age")
    message = request.POST.get("message")

    user = Users(name=name, username=user_name, age=age, message=message)
    user.enrgistrer()
    typer.secho(f"L'utilisateur {name} enregistré avec succés.", fg=typer.colors.GREEN)
    logging.basicConfig(level=logging.INFO,
                        filename='user.log',
                        filemode="a",
                        format="%(asctime)s - %(message)s")
    info = f"l’Utilisateur {name} vient d'être enregistré "
    logging.info(info)

    return redirect('leyssare')#rediriger vers la page forum.html au lieu de index
def del_contact(request):
    name_to_del = request.POST.get("name-to-del")
    print(type(name_to_del))
    user = Users(name="Mamadou", username="Diallo", age=3, message="Longue vie à toi.")
    user_existe = user.del_data(name_to_del)
    if not user_existe:
        typer.secho(f"L'utilisateur {name_to_del} n'existe pas", fg=typer.colors.BLUE)
        return  render(request, "forum.html", {'notVU':name_to_del})
    else:
        typer.secho(f"L'utilsateur {name_to_del} supprimé avec succés.", fg=typer.colors.RED)
        return render(request, "forum.html", {'user_exist':name_to_del})
   # return redirect("leyssare")
