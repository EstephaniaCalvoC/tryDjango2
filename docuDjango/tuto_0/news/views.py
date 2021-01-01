from django.shortcuts import render

# Create your views here.
from .models import Article


def year_archive(request, year):
    a_list = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': a_list}
    return render(request, 'news/year_archive.html', context)


def month_archive(request, year, month):
    a_list = Article.objects.filter(pub_date__year=year, pub_date__month=month)
    context = {'year':year, 'month':month, 'article_list':a_list}
    return render(request, 'news/month_archive.html', context)

def reporter_archive(request, r_name):
    a_list = Article.objects.filter(reporter__full_name=r_name)
    context = {'reporter_name':r_name, 'article_list':a_list}
    return render(request, 'news/reporter_archive.html', context)