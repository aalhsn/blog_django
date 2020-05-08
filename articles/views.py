from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Article
from .forms import ArticleForm, ArticleUpdateForm


# Create your views here.
def homepage_view(request):
    context = {
        "Food": {
            "art1":"Food in Miami",
            "art2":"Food in India"
        },
        "Travel":{
            "cont1":"India",
            "cont2":"Miami",
        }
    }
    return render(request,"home_page.html", context)

def article_detail(request, article_id):
    article = Article.objects.get(id=article_id)
    context = {
        "article":article
    }
    return render(request, 'article_detail_page.html', context)

def article_list(request):
    articles = Article.objects.all()
    context = {
        "articles": articles,
    }
    return render(request, 'article_list_page.html', context)


def create_view(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles-list")
    context = {
        "form":form
    }
    return render(request, 'create_page.html', context)

def update_view(request, article_id ):
    article = Article.objects.get(id=article_id)
    form = ArticleUpdateForm(instance=article)

    if request.method == "POST":
        form = ArticleUpdateForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles-list')

    context = {
        "article":article,
        "form":form
    }
    return render(request, 'update_page.html', context)