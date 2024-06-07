from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse
from django.contrib import messages
from decimal import Decimal, InvalidOperation


from decimal import Decimal, InvalidOperation

def cadastrar_produto(request):
    codigo = request.GET.get('codigo', '')
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
            if produto.valor is None:
                # Caso o campo valor não seja fornecido no formulário, você pode tratar isso de acordo com sua lógica de negócios
                produto.valor = 0.0
            else:
                try:
                    produto.valor = Decimal(str(produto.valor).replace(',', '.'))
                except InvalidOperation:
                    return render(request, 'produtos/cadastrar_produto.html', {
                        'form': form,
                        'error': 'Erro ao cadastrar produto. Valor inválido.',
                    })
            if produto.codigo_fusofix is None:
                produto.codigo_fusofix = ''
            produto.save()
            messages.success(request, 'Produto cadastrado com sucesso!')
            return redirect(f"{reverse('consultar_produto')}?message=Produto cadastrado com sucesso!")
        else:
            return render(request, 'produtos/cadastrar_produto.html', {'form': form, 'error': 'Erro ao cadastrar produto. Por favor, tente novamente.'})
    else:
        form = ProdutoForm(initial={'codigo': codigo})
    return render(request, 'produtos/cadastrar_produto.html', {'form': form})

def atualizar_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        cotacao_efetivada = 'cotacao_efetivada' in request.POST
        data_efetivacao = request.POST.get('data_efetivacao', None)

        # Manualmente pegue os valores dos campos do template
        valor = request.POST.get('valor', None)
        numero_de_pecas = request.POST.get('produto.numero_de_pecas', None)
        pecas_compradas = request.POST.get('pecas_compradas', None)

        # Converter o valor para Decimal
        try:
            if valor is not None:
                valor = valor.replace(',', '.')
                valor = Decimal(valor)
        except InvalidOperation:
            form.add_error('valor', 'O valor deve ser um número decimal válido.')

        if cotacao_efetivada and not data_efetivacao:
    
            form.add_error('data_efetivacao', 'Data da cotação é necessária quando a cotação é efetivada.')
        else:
            if form.is_valid():
                # Atualize manualmente os campos removidos
                produto.valor = valor
                produto.numero_de_pecas = numero_de_pecas
                produto.pecas_compradas = pecas_compradas if pecas_compradas is not None else produto.pecas_compradas
                if cotacao_efetivada:
                    produto.data_efetivacao = data_efetivacao
                else:
                    produto.data_efetivacao = None
                produto.cotacao_efetivada = cotacao_efetivada
                produto.save()
                return redirect(f"{reverse('consultar_produto')}?codigo={codigo}&message=Produto atualizado com sucesso!&success=true")

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/consultar_produto.html', {'form': form, 'produto': produto})

def consultar_produto(request):
    message = request.GET.get('message', None)
    produto = None
    produto_nao_encontrado = False
    if 'codigo' in request.GET:
        codigo = request.GET['codigo']
        produto = Produto.objects.filter(codigo=codigo).first()
        if produto:
            form = ProdutoForm(instance=produto)
        else:
            produto_nao_encontrado = True
    return render(request, 'produtos/consultar_produto.html', {
        'produto': produto,
        'form': ProdutoForm(instance=produto) if produto else ProdutoForm(),
        'codigo': request.GET.get('codigo', ''),
        'produto_nao_encontrado': produto_nao_encontrado,
        'message': message
    })



def excluir_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)
    produto.delete()
    messages.success(request, 'Produto excluído com sucesso.')
    return redirect('consultar_produto')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})
