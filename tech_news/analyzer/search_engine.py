from tech_news.database import db


# https://kb.objectrocket.com/mongo-db/how-to-query-mongodb-documents-with-regex-in-python-362
def search_by_title(title):
    news = db.news.find(
        {"title": {"$regex": title, "$options": "i"}},
        {"title": 1, "url": 1, "_id": 0},
    )
    return [(new["title"], new["url"]) for new in news]


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_source(source):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
