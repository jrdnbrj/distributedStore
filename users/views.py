from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from users.forms import UserForm
from users.models import User
from products.models import Product

def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', { 'products': products })

def create_account(request):
    if request.method == 'POST':
        user = UserForm(request.POST)
        if user.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            if user is None:
                print('User is None')
                redirect('iniciar_sesion')
            return redirect('iniciar_sesion')
        else:
            print(user.errors)
    return render(request, 'login/crear_cuenta.html')

def log_in(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            print('Credenciales incorrectas')
            context['msg'] = 'El usuario o la contraseña es incorrecta, por favor vuelva a intentar.'
            context['username'] = username

    return render(request, 'login/iniciar_sesion.html', context)

@login_required
def sign_off(request):
    logout(request)
    return redirect('index')