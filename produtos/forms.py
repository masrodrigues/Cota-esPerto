from django import forms
from .models import Produto
from decimal import Decimal


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
           
            "nome",
            "descricao_longa",
            "valor",
           'cotacao_efetivada', 'data_efetivacao'
            
        ]
        widgets = {
            
            "nome": forms.TextInput(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none"
                }
            ),
            "descricao_longa": forms.Textarea(
                attrs={
                    "class": "form-input w-full p-2 border border-gray-300 rounded-md focus:outline-none",
                    "style": "height: 130px;",  # Ajuste o valor conforme necessário
                }
            ),
            "valor": forms.TextInput(
                attrs={
                    "class": "form-input bg-yellow-200 w-full p-2 font-bold text-lg border border-gray-300 rounded-md focus:outline-none"
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