import datetime
import requests as req
from bs4 import BeautifulSoup
from fake_headers import Headers

# Задание 1.
# def logger(func):
#     def update_function(*args, **kwargs):
#         with open('info.txt', 'w') as f:
#             call_time = datetime.datetime.now()
#             f.write(f'Дата и время вызова функции - {call_time}\nИмя функции - {func.__name__}\n')
#             f.write(f'Аргументы функции. *args - {args}, *kwargs - {kwargs}')
#         func()
#     return update_function
# @logger
# def hello_world():
#     print('hello world')
# hello_world()


# Задание 2 и 3.
def logger(path):
    def function(func):
        def update_function(*args, **kwargs):
            with open(path, 'w') as f:
                call_time = datetime.datetime.now()
                f.write(f'Дата и время вызова функции - {call_time}\nИмя функции - {func.__name__}\n')
                f.write(f'Аргументы функции. *args - {args}, **kwargs - {kwargs}')
            func(*args, **kwargs)
        return update_function
    return function

@logger('info.txt')
def habr_parser(KEYWORDS):
    url = 'https://habr.com/ru/all/'
    headers = Headers(
        os="win",
        headers=True
    ).generate()
    response = req.get(url, headers=headers)
    text = response.text
    soup = BeautifulSoup(text, features='html.parser')
    list_article = soup.find_all("article")

    for article in list_article:
        hubs = article.find_all(class_= 'tm-article-snippet__hubs-item')
        hubs = [hub.text.lower().strip() for hub in hubs]
        titles = article.find_all(class_= 'tm-article-snippet__title tm-article-snippet__title_h2')
        title = [title.text.lower().strip() for title in titles]
        title_output = [title.text.strip() for title in titles] # Данная переменная для вывода заголовка в исходном виде

        # На разных статьях иногда превью текста находится в разных тегах, из-за этого чтобы избавиться от потери данных
        # Создал две переменные и их будем проверять.
        descriptions = article.find_all(class_= 'article-formatted-body article-formatted-body article-formatted-body_version-2')
        descriptions_2 = article.find_all(class_= 'article-formatted-body article-formatted-body article-formatted-body_version-1')
        descriptions = [description.text.lower().strip() for description in descriptions]
        descriptions_2 = [description.text.lower().strip() for description in descriptions_2]
        all_info = hubs + title + descriptions + descriptions_2
        for word in KEYWORDS:
            word = word.lower().strip()
            if word in all_info or word + ' *' in all_info or word + '*' in all_info:
                href = 'https://habr.com' + article.find(class_= 'tm-article-snippet__title-link').attrs['href']
                published_time = article.find(class_= 'tm-article-snippet__datetime-published').text.strip()
                print(f'Статья найдена по ключевому слову - {word}\nЗаголовок: {title_output[0]}\n\n{published_time}\nСсылка на статью - {href}')
                print("-" * 60)