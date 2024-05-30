from django import forms
from .models import Produto

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            "codigo",
            "nome",
            "descricao_longa",
            "valor",
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
                    "style": "height: 130px;",
                }
            ),
            "valor": forms.TextInput(
                attrs={
                    "class": "form-input bg-yellow-200 w-full p-2 font-bold text-lg border border-gray-300 rounded-md focus:outline-none",
                    "style": "font-bold;",
                }
            ),
        }

    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        if "," in str(valor):
            raise forms.ValidationError(
                "O valor não pode conter vírgula. Use ponto como separador decimal."
            )
        return valor

    def clean(self):
        cleaned_data = super().clean()
        cotacao_efetivada = self.data.get("cotacao_efetivada")
        data_efetivacao = self.data.get("data_efetivacao")

        if cotacao_efetivada and not data_efetivacao:
            self.add_error('data_efetivacao', 'Data da cotação é necessária quando a cotação é efetivada.')

        return cleaned_data
