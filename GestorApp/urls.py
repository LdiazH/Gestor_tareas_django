from django.urls import path, include
from .views import *
from . import views 

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'), 
    path('tareas/', ListaTareas.as_view(), name='tareas'),
    path('tareas/<int:pk>/eliminar/', EliminarTarea.as_view(), name='eliminar_tarea'),
    path('tareas/<int:pk>/', DetalleTarea.as_view(), name='detalle_tarea'),
    path('tareas/<int:pk>/editar/', EditarTarea.as_view(), name='editar_tarea'),
    path('AgregarTareas/', AgregarTarea.as_view(), name='agregar_tarea'),
    path('login/', views.login_view, name="login"),
    #path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('registro/', RegistroUsuario.as_view(), name='registro'),
    path('no_permiso/', NoPermiso.as_view(), name='no_permiso'),
    path('registro_exitoso/', RegistroExitoso.as_view(), name='registro_exitoso'),
    
       
    
]