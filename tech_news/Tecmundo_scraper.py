class Scrap_tecmundo:
    def __init__(self, selector) -> None:
        self.selector = selector
        self.url = selector.css("head > link[rel=canonical]::attr(href)").get()
        self.title = selector.css(".tec--article__header__title::text").get()
        self.time = selector.css("time::attr(datetime)").get()
        self.writer = selector.css(".tec--author__info__link::text").get()
        # no idea why this works since array returns False
        self.shares_count = (
            int(selector.css(".tec--toolbar__item::text").re(r"\d+")[0])
            if selector.css(".tec--toolbar__item::text").re(r"\d+")
            else 0
        )
        self.comments_count = int(
            selector.css("#js-comments-btn::text").re(r"\d+")[0]
        )
        self.summary = "".join(
            selector.css(".tec--article__body > p *::text").getall()
        )
        # > doest work, only empty space
        self.sources = [
            source.strip()
            for source in selector.css(
                ".tec--article__body-grid  div:nth-child(6) *::text"
            ).getall()
            if source not in [" ", "Fontes"]
        ]

    def mount(self):
        a = self.selector.css(
            ".tec--article__body-grid  div:nth-child(6) *::text"
        ).getall()
        for source in a:
            print(type(source))
