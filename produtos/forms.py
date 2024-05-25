from django import forms
from .models import Produto
from decimal import Decimal


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "codigo",
            "codigo_fusofix",
            "nome",
            "descricao_longa",
            "valor",
            "cotacao_efetivada",
            
        ]
        widgets = {
            "codigo": forms.TextInput(
                attrs={
                    "class": "form-input w-full p-2 font-bold border border-gray-300 rounded-md focus:outline-none"
                }
            ),
            "codigo_fusofix": forms.TextInput(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none"
                }
            ),
            "nome": forms.TextInput(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none"
                }
            ),
            "descricao_longa": forms.Textarea(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none",
                    "style": "height: 150px;",  # Ajuste o valor conforme necessário
                }
            ),
            "valor": forms.TextInput(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none"
                }
            ),
           
        }

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        # Converte o valor para string antes de verificar a vírgula
        if "," in str(valor):
            raise forms.ValidationError(
                "O valor não pode conter vírgula. Use ponto como separador decimal."
            )
        return valor