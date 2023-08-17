# blog/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Articulo
from .forms import ArticuloForm

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def article_list(request):
    article = Articulo.objects.all()
    return render(request, 'blog/article_list.html', {'article': article})

@login_required
def create_article(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.autor = request.user
            article.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticuloForm()
    return render(request, 'blog/create_article.html', {'form': form})

@login_required
def edit_article(request, article_id):
    article = get_object_or_404(Articulo, pk=article_id)
    if article.autor != request.user:
        return redirect('article_detail', article_id=article.id)
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', article_id=article.id)
    else:
        form = ArticuloForm(instance=article)
    return render(request, 'blog/edit_article.html', {'form': form, 'article': article})

@login_required
def delete_article(request, article_id):
    article = get_object_or_404(Articulo, pk=article_id)
    if article.autor != request.user:
        return redirect('article_detail', article_id=article.id)
    if request.method == 'POST':
        article.delete()
        return redirect('article_list')
    return render(request, 'blog/delete_article.html', {'article': article})

def article_detail(request, article_id):
    article = get_object_or_404(Articulo, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
