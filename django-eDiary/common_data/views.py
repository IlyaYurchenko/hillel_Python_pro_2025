from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login_handler(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'profile.html', {'user': user})
        else:
            return render(request, '/login.html', {"error ": "Invalid credentials"})
    else:
        return render(request, 'login.html')


def logout_handler(request):
    logout(request)
    return redirect('login')

def register_handler(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        try:
            User.objects.get(username=username)
            return render(request, '/register.html', {"error ": "Username already exists"})
        except User.DoesNotExist:
            pass

        new_user = User.objects.create_user(
            username=username,
            first_name=firstname,
            last_name=lastname,
            password=password,
            email=email
        )
        new_user.save()
        return redirect('/login')

    else:
        return render(request, 'register.html')
