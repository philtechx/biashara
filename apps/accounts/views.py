from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def register_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Akaunti imeundwa kwa mafanikio. Tafadhali ingia.")
        return redirect("login")
    
    return render(request, "accounts/register.html")

def login_view(request):
    if request.method == "POST":
        # Handle login logic here
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username au Password si sahihi")
    return render(request, "login.html")

