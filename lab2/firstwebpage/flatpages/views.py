# Описание: Представления (views) для приложения flatpages с поддержкой шаблонов

# Импорт функции render из модуля django.shortcuts
# render - функция для рендеринга (отображения) шаблонов
# Принимает запрос, путь к шаблону и контекст (данные для шаблона)
# Аналогичная реализация: render(request, 'template.html', {'key': 'value'})
from django.shortcuts import render

# Импорт модуля template из django
# Используется для работы с шаблонной системой Django
from django import template


# Функция-представление home с использованием шаблона
def home(request):
    return render(request, 'templates/static_handler.html')



