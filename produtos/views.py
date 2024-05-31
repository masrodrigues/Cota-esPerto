from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto
from .forms import ProdutoForm
from django.urls import reverse
from django.contrib import messages

def cadastrar_produto(request):
    codigo = request.GET.get('codigo', '')
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            produto = form.save(commit=False)
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

def atualizar_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        cotacao_efetivada = 'cotacao_efetivada' in request.POST
        data_efetivacao = request.POST.get('data_efetivacao', None)

        if cotacao_efetivada and not data_efetivacao:
            form.add_error('data_efetivacao', 'Data da cotação é necessária quando a cotação é efetivada.')
        else:
            if form.is_valid():
                if cotacao_efetivada:
                    produto.data_efetivacao = data_efetivacao
                else:
                    produto.data_efetivacao = None
                produto.cotacao_efetivada = cotacao_efetivada
                form.save()
                return redirect(f"{reverse('consultar_produto')}?codigo={codigo}&message=Produto atualizado com sucesso!&success=true")

    else:
        form = ProdutoForm(instance=produto)

    return render(request, 'produtos/consultar_produto.html', {'form': form, 'produto': produto})

def excluir_produto(request, codigo):
    produto = get_object_or_404(Produto, codigo=codigo)
    produto.delete()
    messages.success(request, 'Produto excluído com sucesso.')
    return redirect('consultar_produto')

def listar_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'produtos/listar_produtos.html', {'produtos': produtos})
