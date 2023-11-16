from django import forms
from apps.biblioteca.models import Livro

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Livro
        exclude = ['publicada', 'usuario', ]
        labels = {
            'observação': 'Observação',
            'data_entrada': "Data de Registro",
            'usuario': "Usuário",
            'nome_popular': 'Nome Popular',
            'data_saida': 'Data Saída',
            }
        widgets = {
            "nome_popular": forms.TextInput(attrs={"class": "form-control"}),
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "especie": forms.TextInput(attrs={"class": "form-control"}),
            "classe": forms.Select(attrs={"class": "form-control"}),
            "observação": forms.Textarea(attrs={"class": "form-control"}),
            "sexo": forms.Select(attrs={"class": "form-control"}),
            "foto": forms.FileInput(attrs={"class": "form-control"}),
            "data_entrada": forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "class": "form-control",
                    "type": "date",
                }),
            "origem": forms.TextInput(attrs={"class": "form-control"}),
            "data_saida": forms.DateInput(
                format="%d/%m/%Y",
                attrs={
                    "class": "form-control",
                    "type": "date",
                }),
            "motivo": forms.TextInput(attrs={"class": "form-control"}
            ),
            
        }

