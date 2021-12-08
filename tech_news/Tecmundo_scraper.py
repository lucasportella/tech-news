class Scrap_tecmundo:
    def __init__(self, selector) -> None:
        self.selector = selector
        self.url = selector.css("head > link[rel=canonical]::attr(href)").get()
        self.title = selector.css(".tec--article__header__title::text").get()
        self.timestamp = selector.css("time::attr(datetime)").get()
        self.writer = self.find_writer()
        # no idea why this works since array returns False
        self.shares_count = (
            int(selector.css(".tec--toolbar__item::text").re(r"\d+")[0])
            if selector.css(".tec--toolbar__item::text").re(r"\d+")
            else 0
        )
        self.comments_count = (
            int(selector.css("#js-comments-btn::text").re(r"\d+")[0])
            if selector.css("#js-comments-btn::text").re(r"\d+")
            else 0
        )
        self.summary = "".join(
            selector.css(
                ".tec--article__body > p:nth-child(1) *::text"
            ).getall()
        )
        # > doest work, only empty space
        self.sources = [
            source.strip()
            for source in selector.css(
                ".z--mb-16 > div > a::text"
            ).getall()
            if source not in [" ", "Fontes"]
        ]
        self.categories = [
            category.strip()
            for category in selector.css("#js-categories *::text").getall()
            if category != " "
        ]

    def find_writer(self):
        query_selectors = [
            ".tec--author__info__link::text",
            ".tec--timestamp a::text",
            "#js-author-bar > div p::text",
        ]
        for query in query_selectors:
            result = self.selector.css(query).get()
            if result is not None:
                print(result)
                return result.strip()
        return None

    def mount(self):
        return {
            "url": self.url,
            "title": self.title,
            "timestamp": self.timestamp,
            "writer": self.writer,
            "shares_count": self.shares_count,
            "comments_count": self.comments_count,
            "summary": self.summary,
            "sources": self.sources,
            "categories": self.categories,
        }
