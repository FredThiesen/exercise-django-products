from django.shortcuts import render
from .models import Produto, Categoria

# Create your views here.


def index(request):
    return render(request, 'produtos/index.html')


def produtos(request):
    categoria_id = request.GET.get('categoria')
    
    if categoria_id:
        produtos = Produto.objects.filter(categoria_id=categoria_id)
    else:
        produtos = Produto.objects.all()
    
    produtos = produtos.order_by('categoria__nome', 'nome')
    categorias = Categoria.objects.all()
    
    return render(request, 'produtos/produtos.html', {
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': int(categoria_id) if categoria_id else None
    })