from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.views.generic.edit import DeleteView, UpdateView
from .models import Tarea
from .formularios import TareaForm, RegistroUsuario
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin   
from django.contrib.auth import authenticate, login, logout 

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'
    
    
class ListaTareas(LoginRequiredMixin, ListView):
    model = Tarea
    template_name = 'tareas.html'
    context_object_name = 'tareas'  
    login_url = 'login' 
    
   # def get_queryset(self):
        # Solo las tareas del usuario actual
        #return Tarea.objects.filter(usuario=self.request.user)
    
class EliminarTarea(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Tarea
    template_name = 'eliminar_tarea.html'
    success_url = reverse_lazy('tareas')
    login_url = 'login'

    def test_func(self):
        tarea = self.get_object()
        return self.request.user == tarea.usuario
    
    def handle_no_permission(self):
        # Redirige a un template de "No tienes permiso"
        from django.shortcuts import render
        return render(self.request, 'no_permiso.html')

class DetalleTarea(LoginRequiredMixin, DetailView):
    model = Tarea
    template_name = 'detalle_tarea.html'
    context_object_name = 'tarea'
    login_url = 'login'
    
class AgregarTarea(LoginRequiredMixin, CreateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'agregar_tarea.html'

    success_url = reverse_lazy('tareas')
    login_url = 'login'
   
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
class EditarTarea(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Tarea
    form_class = TareaForm
    template_name = 'editar_tarea.html'
    success_url = reverse_lazy('tareas')
    login_url = 'login'

    def test_func(self):
        tarea = self.get_object()
        return self.request.user == tarea.usuario
    def handle_no_permission(self):
        # Redirige a un template de "No tienes permiso"
        from django.shortcuts import render
        return render(self.request, 'no_permiso.html')
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        usuario = authenticate(request, username=username, password=password) #Verifica si el usuario existe en la base de datos
        if usuario is not None:
            login(request, usuario) #Crea la sesión del usuario
            return redirect('home') #Redirige a la página de inicio
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)# funcion hecha de moedelo auth que elimina la sesion actual
    return redirect('login')


class RegistroUsuario(CreateView):
    template_name = 'registro.html'
    form_class = RegistroUsuario
    success_url = reverse_lazy('registro_exitoso')
    
class NoPermiso(TemplateView):
    template_name = 'no_permiso.html'
    
class RegistroExitoso(TemplateView):
    template_name = 'registro_exitoso.html'
    
    