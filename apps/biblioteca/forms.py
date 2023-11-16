from django import forms
from apps.biblioteca.models import Livro

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ['publicada',]
        labels = {
            "observação": 'Observação',
            'data_fotografia': "Data de Registro",
            'usuario': "Usuário",
            }
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "especie": forms.TextInput(attrs={"class": "form-control"}),
            "nome_popular": forms.TextInput(attrs={"class": "form-control"}),
            "classe": forms.Select(attrs={"class": "form-control"}),
            "Observação": forms.Textarea(attrs={"class": "form-control"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "usuario": forms.Select(attrs={"class": "form-control"}),
            "data_fotografia": forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),
            
        }

