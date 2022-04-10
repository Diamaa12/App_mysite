from django.shortcuts import render, redirect
from django.shortcuts import render, HttpResponse
from webapp.user_class.users import Users

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
    print("Data saved with success.")
    return redirect('index')#rediriger vers la page forum.html au lieu de index

