import lxml.html as html
from urllib.request import urlopen
import json

main_domain_stat = 'https://habr.com/'


def main():
    articles = []
    main_page = html.parse(
        urlopen(main_domain_stat)
    ).getroot()

    article_links = main_page.xpath(
        '//li/article[contains(@class,"post")]/h2[@class="post__title"]/a[@class="post__title_link"]/@href'
    )

    for link in article_links:
        article_page = html.parse(
            urlopen(link)
        )
        article_title = article_page.xpath(
            '//div[@class="post__wrapper"]/h1[contains(@class,"post__title")]/span/text()'
        )
        article_text = article_page.xpath(
            '//div[@class="post__wrapper"]/div[contains(@class,"post__body")]/div[contains(@class,"post__text")]//text()'
        )
        article_pics = article_page.xpath(
            '//div[@class="post__wrapper"]/div[contains(@class,"post__body")]/div[contains(@class,"post__text")]//img/@src'
        )
        articles.append({
            'title': article_title[0],
            'text': ''.join(article_text),
            'pics': article_pics
        })

    with open('articles.json', 'w') as json_data:
        json.dump(articles, json_data, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
