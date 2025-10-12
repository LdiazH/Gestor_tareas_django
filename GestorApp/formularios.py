from django import forms
from .models import Tarea
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


#Formularios de tareas

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['titulo', 'descripcion', 'fecha_limite', 'completada']
        labels = {
            'titulo': 'Título',
            'descripcion': 'Descripción',
            'fecha_limite': 'Fecha de Vencimiento',
            'completada': 'Completada',
        }
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Escribe un título breve para la tarea',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Agrega una descripción opcional...',
            }),
            'fecha_limite': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'completada': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

#Formulario resgistro de usuarios        
        
class RegistroUsuario(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']  # solo usuario y contraseñas
        labels = {
            'username': 'Nombre de usuario',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }