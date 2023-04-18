from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from .forms import TarefaForm, UsuarioForm
from .models import Tarefa


def home(request):
    tarefas = Tarefa.objects.all()
    context = {
        'tarefas': tarefas,
    }
    return render(request, 'home.html', context)


def criar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            # Cria o novo usuário com o username, email e senha fornecidos no formulário
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            # Loga o usuário automaticamente após o cadastro
            user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, user)

            return redirect('home')
    else:
        form = UsuarioForm()

    return render(request, 'criar_usuario.html', {'form': form})


def criar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm()
    return render(request, 'criar_tarefa.html', {'form': form})


def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        form = TarefaForm(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TarefaForm(instance=tarefa)  # passa o instance para o form

    context = {
        'form': form,
        'tarefa': tarefa,  # adiciona a tarefa ao contexto
    }
    return render(request, 'editar_tarefa.html', {'form': form})


def deletar_tarefa(request, tarefa_id):
    # Busca a tarefa pelo ID ou retorna um erro 404 se ela não existe
    tarefa = get_object_or_404(Tarefa, pk=tarefa_id)

    if request.method == 'POST':
        tarefa.delete()
        return redirect('home')

    return render(request, 'deletar_tarefa.html', {'tarefa': tarefa})
