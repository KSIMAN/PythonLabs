# Импортирую модуль административной панели
from django.contrib import admin
# Импортирую созданную модель Article из текущего приложения
# Точка перед models означает импорт из текущей директории
from .models import Article

# Создаю класс для настройки отображения модели в админке
# Наследую от admin.ModelAdmin - базовый класс для настройки
class ArticleAdmin(admin.ModelAdmin):
    # list_display - кортеж полей для отображения в списке статей
    # title - заголовок статьи
    # author - автор статьи
    # get_excerpt - метод модели для отображения отрывка
    # created_date - дата создания
    list_display = ('title', 'author', 'get_excerpt', 'created_date')
    
    # Можно добавить дополнительные настройки:
    # list_filter = ('created_date', 'author')  # Фильтры в боковой панели
    # search_fields = ('title', 'text')  # Поля для поиска

# Регистрирую модель в административной панели
# Первый параметр - модель для регистрации
# Второй параметр - класс с настройками отображения
admin.site.register(Article, ArticleAdmin)