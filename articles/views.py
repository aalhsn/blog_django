from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.generics import ListAPIView
from .serializers import ArticlesListSerializer
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
    food_types = article.food_type.all()
    context = {
        "article":article,
        "food_types":food_types
    }
    return render(request, 'article_detail_page.html', context)

class ArticlesListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticlesListSerializer


def create_view(request):
    form = ArticleForm()

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
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
        form = ArticleUpdateForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles-list')

    context = {
        "article":article,
        "form":form
    }
    return render(request, 'update_page.html', context)

def delete_article(request, article_id):
    article = Article.objects.get(id=article_id).delete()
    return redirect('articles-list')

