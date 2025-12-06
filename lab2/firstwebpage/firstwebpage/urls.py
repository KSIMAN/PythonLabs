# Описание: Маршрутизация URL-адресов проекта

# Импорт функции admin из модуля django.contrib
# admin - модуль для работы с административной панелью
from django.contrib import admin

# Импорт функции path из модуля django.urls
# path - функция для определения URL-маршрутов
# Аналогичная реализация: path('адрес/', функция_представления, name='имя')
from django.urls import path

# Импорт представлений (views) из приложения flatpages
# Это позволяет использовать функции из файла views.py
# Аналогичная реализация: from my_app import views
from flatpages import views


# urlpatterns - список URL-маршрутов проекта
# Каждый маршрут связывает URL-адрес с функцией-представлением
# Аналогичная реализация: routes = [route1, route2, route3]
urlpatterns = [
    # Маршрут для административной панели
    # path('admin/', admin.site.urls) - доступ к админке по адресу /admin/
    path('admin/', admin.site.urls),
    
    # Маршрут для главной страницы
    # '' - пустая строка означает корневой URL (http://127.0.0.1:8000/)
    # views.home - функция-представление, которая обрабатывает этот запрос
    # name='home' - имя маршрута для обращения к нему из других частей проекта
    # Аналогичная реализация: path('about/', views.about, name='about')
    path('', views.home, name='home'),
    ]
