# Стандартные библиотеки.
from django.urls import path

# Локальные импорты
from . import views


app_name = 'pages'


urlpatterns = [
    path(
        'about/',
        views.about,
        name='about',
    ),
    path(
        'rules/',
        views.rules,
        name='rules',
    ),
]
