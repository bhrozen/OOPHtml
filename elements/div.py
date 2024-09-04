from elements.html import HtmlElement


class DivElement(HtmlElement):

    def __init__(self, content: str):
        self.content = content

    def to_html(self):
        return f"<div>{self.content}</div>"
