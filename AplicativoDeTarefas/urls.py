"""
URL configuration for AplicativoDeTarefas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appTarefas.views import criar_tarefa, home, criar_usuario, editar_tarefa, deletar_tarefa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nova/', criar_tarefa, name='criar_tarefa'),
    path('', home, name='home'),
    path('criar_usuario/', criar_usuario, name='criar_usuario'),
    path('editar_tarefa/<int:pk>/', editar_tarefa, name='editar_tarefa'),
    path('deletar_tarefa/<int:tarefa_id>/', deletar_tarefa, name='deletar_tarefa'),

]
