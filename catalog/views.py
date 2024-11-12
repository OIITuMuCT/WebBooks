from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    text_head = 'Это заголовок главной страницы сайта'
    text_body = 'Это содержимое главной страницы сайта'
    context = {'text_head': text_head, 'text_body': text_body}
    # передача словаря context с данным в шаблон
    return render(request, 'catalog/index.html', context)
