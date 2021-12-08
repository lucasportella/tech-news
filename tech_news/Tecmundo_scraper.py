class Scrap_tecmundo:
    def __init__(self, selector) -> None:
        self.selector = selector
        self.url = self.selector.css("head > link[rel=canonical]::attr(href)").get()
