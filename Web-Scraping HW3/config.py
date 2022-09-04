import requests as req
from bs4 import BeautifulSoup
from fake_headers import Headers


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
        hubs = [hub.text.strip() for hub in hubs]
        title = article.find_all(class_= 'tm-article-snippet__title tm-article-snippet__title_h2')
        title = [title.text.strip() for title in title]
        # На разных статьях иногда превью текста находится в разных тегах, из-за этого чтобы избавиться от потери данных
        # Создал две переменные и их будем проверять.
        descriptions = article.find_all(class_= 'article-formatted-body article-formatted-body article-formatted-body_version-2')
        descriptions_2 = article.find_all(class_= 'article-formatted-body article-formatted-body article-formatted-body_version-1')
        descriptions = [description.text.strip() for description in descriptions]
        descriptions_2 = [description.text.strip() for description in descriptions_2]
        all_info = hubs + title + descriptions + descriptions_2

        for word in KEYWORDS:
            if word in all_info or word + ' *' in all_info:
                href = 'https://habr.com' + article.find(class_= 'tm-article-snippet__title-link').attrs['href']
                published_time = article.find(class_= 'tm-article-snippet__datetime-published').text.strip()
                print(f'Статья найдена по ключевому слову - {word}\nЗаголовок: {title[0]}\n\n{published_time}\nСсылка на статью - {href}')
                print("-" * 60)

