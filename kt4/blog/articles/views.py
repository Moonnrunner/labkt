from django.shortcuts import render
from .models import Article
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django import template


def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
def all(request):
	return render(request, 'articles.html', {"posts": Article.objects.all()})