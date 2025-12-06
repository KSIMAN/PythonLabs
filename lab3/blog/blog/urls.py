# Импорт модуля admin для административной панели
from django.contrib import admin
# Импорт функции path для определения URL-маршрутов
from django.urls import path
# Импорт представлений из приложения articles
# articles - название приложения (директории)
# views - модуль с функциями-представлениями
from articles import views

# urlpatterns - список URL-маршрутов проекта
urlpatterns = [
    # Маршрут для административной панели
    path('admin/', admin.site.urls),
    
    # Маршрут для главной страницы - отображает архив статей
    # '' - пустая строка означает корневой URL (http://127.0.0.1:8000/)
    # views.archive - функция-представление для обработки запроса
    # name='archive' - имя маршрута для обращения к нему из других частей проекта
    path('', views.archive, name='archive'),
]
