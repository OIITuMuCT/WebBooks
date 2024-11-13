from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView

from .models import Book, Author, BookInstance

# Create your views here.
def about(request):
    text_head = 'Сведения о компании'
    name = 'OOO "Интеллектуальные информационные системы"'
    rab1 = 'Разработка приложений на основе систем искусственного интеллекта'
    rab2 = 'Распознавание объектов дорожной инфраструктуры'
    rab3 = 'Создание графических АРТ-объектов на основе систем искусственного интеллекта'
    rab4 = 'Создание цифровых интерактивных книг, учебных пособий автоматизированных обучающих систем'
    context = {'text_head':text_head, 'rab1': rab1, 'rab2':rab2, 'rab3':rab3, 'rab4': rab4}
    return render(request, 'catalog/about.html', context)

def contact(request):
    text_head = 'Контакты'
    name = 'ООО "Интеллектуальные информационные системы'
    address = 'Москва, ул. Планерная, д. 20, к. 1'
    tel = '495-345-45-45'
    email = 'iis_info@example.com'
    # Словарь для передачи данных в шаблон index.html
    context = {
        'text_head': text_head,
        'name': name,
        'address': address,
        'tel': tel,
        'email': email,
    }
    # Передача словаря context с данными в шаблон
    return render(request, 'catalog/contact.html', context)

def index(request):
    text_head = 'На нашем сайте вы можете получить книги в электронном виде'
    # данные о книгах и их количестве
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    # Данные об экземплярах книг в БД
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = "На складе")
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    # Данные об авторах книг
    authors = Author.objects.all()
    num_authors = Author.objects.count()
    # Словарь для передачи данных в шаблон index.html
    context = {'text_head': text_head, 'books': books, 'num_books': num_books, 
               'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors': authors, 'num_authors': num_authors}
    # передача словаря context с данным в шаблон
    return render(request, 'catalog/index.html', context)

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3

class BookDetailView(DeleteView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalog/book_detail.html'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4
    template_name = 'catalog/author_list.html'

class AuthorDetailView(DeleteView):
    model = Author
    context_object_name = 'author'
    template_name = 'catalog/author_detail.html'


