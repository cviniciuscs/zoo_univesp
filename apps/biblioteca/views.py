from django.shortcuts import render, get_object_or_404, redirect
from apps.biblioteca.models import Livro
from django.contrib import messages, auth
from apps.biblioteca.forms import FotografiaForms
from django.contrib.auth.models import User, Group


def index(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    fotografias = Livro.objects.order_by('-id').filter(publicada=True)
    return render(request, 'galeria/index.html', {"cards": fotografias})

def imagem(request, foto_id):
    fotografia = get_object_or_404(Livro, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": fotografia})

def buscar(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    
    fotografias = Livro.objects.order_by('id').filter(publicada=True)

    if "buscar" in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome_popular__icontains = nome_a_buscar)

    return render(request, 'galeria/index.html', {"cards": fotografias})

def nova_imagem(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')

    form = FotografiaForms()
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Novo livro cadastrada!")
            return redirect('index')

    return render(request, 'galeria/nova_imagem.html', {'form': form})

def editar_imagem(request, foto_id):
    if request.user.is_staff:
        fotografia = Livro.objects.get(id=foto_id)
        form = FotografiaForms(instance=fotografia)

        if request.method == 'POST':
            form = FotografiaForms(request.POST, request.FILES, instance=fotografia)
            if form.is_valid():
                form.save()
                messages.success(request, "Cadastro atualizado!")
                return redirect('imagem', foto_id)

    return render(request, 'galeria/editar_imagem.html', {'form': form, 'foto_id': foto_id})

def deletar_imagem(request, foto_id):
    if request.user.is_staff:
        fotografia = Livro.objects.get(id=foto_id)
        fotografia.delete()
        messages.success(request, "Deleção feita com sucesso!")
        return redirect('index')

def filtro(request, classe):
    fotografias = Livro.objects.order_by('id').filter(publicada=True, classe=classe)
    
    return render(request, 'galeria/index.html', {"cards": fotografias})