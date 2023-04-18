from django import forms
from .models import Tarefa
from django.contrib.auth.models import User


class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'usuario']


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
