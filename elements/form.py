from elements.html import HtmlElement


class FormElement(HtmlElement):

    def __init__(self, content: str):
        self.content = content

    def to_html(self):
        return f"<form>{self.content}</form>"
