from elements.html import HtmlElement


class ImgElement(HtmlElement):

    def __init__(self, src: str, alt: str):
        self.src = src
        self.alt = alt

    def to_html(self):
        return f"<img src='{self.src}' alt='{self.alt}' />"
