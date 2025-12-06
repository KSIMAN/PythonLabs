# Импорт модели Article из текущего приложения
# .models - точка означает текущий пакет (директорию articles)
# Article - класс модели статей
from .models import Article

# Импорт функции render из django.shortcuts
# render - функция для рендеринга шаблонов
# Принимает запрос, путь к шаблону и контекст (словарь с данными)
from django.shortcuts import render
# Функция-представление archive - отображает список всех статей
# request - объект HTTP-запроса, автоматически передается Django
def archive(request):
    # Функция render() выполняет рендеринг шаблона и возвращает HTTP-ответ
    # Первый аргумент - объект запроса (request)
    # Второй аргумент - путь к файлу шаблона
    # Третий аргумент - контекст (словарь с данными для шаблона)
       
    # Article.objects.all() - получение всех записей модели Article
    # objects - менеджер модели, предоставляет методы для работы с БД
    # all() - метод для получения всех записей из таблицы
    # {"posts": Article.objects.all()} - словарь контекста
    # "posts" - ключ, по которому данные доступны в шаблоне
    # Article.objects.all() - значение, список всех статей

    return render(request, 'archive.html', {"posts": Article.objects.all()})
