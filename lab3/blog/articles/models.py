# Описание: Модели данных для приложения articles

# Импорт модуля models из django.db
# models - модуль, содержащий классы для создания моделей данных
# Модель в Django - это класс, описывающий структуру таблицы в базе данных
# Аналогичная реализация: from django.db import models
from django.db import models

# Импорт модели User из модуля django.contrib.auth.models
# User - встроенная модель Django для представления пользователей
# Используется для связи статьи с автором
# Аналогичная реализация: from myapp.models import MyModel
from django.contrib.auth.models import User


# Класс Article - модель для хранения статей блога
# models.Model - базовый класс для всех моделей Django
# Наследование от models.Model добавляет функциональность работы с базой данных
# Аналогичная реализация: class MyModel(models.Model): ...
class Article(models.Model):
    
    # Поле title - заголовок статьи
    # models.CharField - тип поля для хранения строк ограниченной длины
    # max_length=200 - максимальная длина строки в символах
    # Аналогичная реализация: name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    
    # Поле author - автор статьи
    # models.ForeignKey - тип поля для создания связи "многие к одному"
    # User - модель, с которой устанавливается связь
    # on_delete=models.CASCADE - при удалении пользователя удаляются его статьи
    # CASCADE означает каскадное удаление связанных записей
    # Аналогичная реализация: category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Поле text - текст статьи
    # models.TextField - тип поля для хранения текста неограниченной длины
    # Используется для больших текстов, в отличие от CharField
    # Аналогичная реализация: description = models.TextField()
    text = models.TextField()
    
    # Поле created_date - дата создания статьи
    # models.DateField - тип поля для хранения даты
    # auto_now_add=True - автоматически устанавливает дату при создании записи
    # Дата устанавливается только один раз при создании и не изменяется
    # Аналогичная реализация: updated_date = models.DateField(auto_now=True) - обновляется при каждом сохранении
    created_date = models.DateField(auto_now_add=True)

    # Метод __unicode__ - возвращает строковое представление объекта
    # Используется для отображения объекта в административной панели и в консоли
    # %s - форматирование строки, подставляет значения из кортежа
    # self.author.username - имя пользователя автора статьи
    # self.title - заголовок статьи
    # Аналогичная реализация: def __str__(self): return self.name
    def __unicode__(self):
        return "%s: %s" % (self.author.username, self.title)
    
    # Метод get_excerpt - возвращает краткое описание статьи
    # Используется для отображения превью текста в списке статей
    # self.text[:140] - срез строки, первые 140 символов
    # Тернарный оператор: результат_если_истина if условие else результат_если_ложь
    # len(self.text) - длина текста статьи
    # Если текст длиннее 140 символов, добавляется "..." в конце
    # Аналогичная реализация: return self.text[:100] + "..." if len(self.text) > 100 else self.text
    def get_excerpt(self):
        return self.text[:140] + "..." if len(self.text) > 140 else self.text