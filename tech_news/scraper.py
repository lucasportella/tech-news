import requests
from parsel import Selector
from time import sleep
from tech_news.Tecmundo_scraper import Scrap_tecmundo


# Requisito 1
# https://softbranchdevelopers.com/python-requests-library-exception-handling-advanced-request-get-parameters/#all-exceptions
def fetch(url):
    resp = ""
    try:
        sleep(1)
        resp = requests.get(url, timeout=3)
    except requests.exceptions.RequestException:
        return None
    finally:
        if resp != "" and resp.status_code == 200:
            return resp.text
        return None


# Requisito 2
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    scraped_news = Scrap_tecmundo(selector)
    return scraped_news.mount()


# Requisito 3
# header Notícias have more hidden news with class .tec--card__title__link, so
#  use id #js-main to restrict to only main news
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    fresh_news = selector.css(
        "#js-main .tec--card__title__link::attr(href)"
    ).getall()
    return fresh_news


# Requisito 4
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page = selector.css("#js-main .tec--btn::attr(href)").get()
    return next_page


# Requisito 5
def get_tech_news(amount):
    pagination = ''
    html_content = fetch(f"https://www.tecmundo.com.br/novidades" + {pagination})
    latest_news = scrape_novidades(html_content)
    while len(latest_news) < amount:
        html_content2 = scrape_next_page_link(html_content)
    #     latest_news.extend(scrape_novidades(html_content))
    # print(len(latest_news))


get_tech_news(60)
