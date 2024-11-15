from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.decorators import login_required
from modernize_se_mercado.forms import UserCadastroCreationForm, LoginForm, OfertaForm
from modernize_se_mercado.models import UserCadastro, Oferta


def index(request):
    return render(request, 'index.html')

def mercados_parceiros(request):
    return render(request, 'mercados_parceiros.html')

def adicionar_ofertas(request):
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('minhas_ofertas')
        else:
            print('nao cadastrado', form.errors)
    else:
        form = OfertaForm()
    return render(request, 'adicionar_ofertas.html', {'form': form})

def deletar_oferta(request, oferta_id):
    oferta = Oferta.objects.get(id=oferta_id)
    oferta.delete()
    return redirect('minhas_ofertas')

def editar_oferta(request, oferta_id):
    oferta = Oferta.objects.get(id=oferta_id)
    if request.method == 'POST':
        form = OfertaForm(request.POST, request.FILES, instance=oferta)
        if form.is_valid():
            form.save()
            return redirect('minhas_ofertas')
    else:
        form = OfertaForm(instance=oferta)
    return render(request, 'editar_ofertas.html', {'form': form, 'oferta': oferta})

def minhas_ofertas(request):
    ofertas = Oferta.objects.all()
    print(ofertas)
    return render(request, 'minhas_ofertas.html', {'ofertas': ofertas})

def perfil_mercado(request):
    return render(request, 'perfil_mercado.html')

def perfil_mercado_editar(request):
    return render(request, 'perfil_mercado_editar.html')

def gerenciador_perfil_mercado(request):
    return render(request, 'gerenciador_perfil_mercado.html')

def login_views(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            lembrar_me = form.cleaned_data.get('remember_me')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                if lembrar_me:
                    request.session.set_expiry(1209600)
                else:
                    request.session.set_expiry(0)
                return redirect('gerenciador_perfil_mercado')
            else:
                form.add_error(None, 'O email ou senha estão incorretos')
    else:
        form = LoginForm()
    return render (request, 'login.html', {'form': form})

def cadastro (request):
    if request.method == 'POST':
        form = UserCadastroCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            data = { key: value for key, value in form.cleaned_data.items() if not (key.startswith('password')) }
            data['password'] = form.cleaned_data.get('password1')

            user = UserCadastro.objects.create_user(
                username=form.cleaned_data.get('nome_mercado'), 
                **data
            )

            print(f"Usuário {user.username} cadastrado com sucesso")
            auth_login(request, user)
            return redirect('login')
        else:
            print('Formulário inváliido')
    else:
        form = UserCadastroCreationForm()
    return render(request, 'cadastro.html', {'form': form})