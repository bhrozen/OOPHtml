from elements.html import HtmlElement


class AElement(HtmlElement):

    def __init__(self, href: str, link_name: str):
        self.href = href
        self.link_name = link_name

    def to_html(self):
        return f"<a href='{self.href}'>{self.link_name}<a>"
