from django.http import HttpResponse

def index(requete):
    return HttpResponse("<h1>Ceci est le message dans la vue</h1>")