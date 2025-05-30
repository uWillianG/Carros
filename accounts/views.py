from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST) #request.post o sistema pega o que o usuário preencheu e o que deseja fazer
        if user_form.is_valid():
            user_form.save()
            return redirect('login') #leva ele para a tela de login
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == "POST": #verificando se o que o usuário preencheu é válido para acessar o sistema
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('cars_list') #se o usuário for válido, leva ele para a tela de lista de carros
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm() #vai trazer o formulário de login vazio
    return render(request, 'login.html', {'login_form': login_form})

def logout_view(request):
    logout(request)
    return redirect('cars_list') #se o usuário não for válido, leva ele para a tela de lista de carros