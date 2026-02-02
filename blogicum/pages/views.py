# Стандартные библиотеки
from django.shortcuts import render


def about(request):
    """
    Отображает страницу о сайте.

    Использует шаблон 'pages/about.html'.

    Args:
        request: HTTP‑запрос.

    Returns:
        HttpResponse: отрендеренный шаблон страницы.
    """
    return render(request, 'pages/about.html')


def rules(request):
    """
    Отображает страницу с правилами.

    Использует шаблон 'pages/rules.html'.

    Args:
        request: HTTP‑запрос.

    Returns:
        HttpResponse: отрендеренный шаблон страницы.
    """
    return render(request, 'pages/rules.html')
