from elements.html import HtmlElement


class InputElement(HtmlElement):

    def __init__(self, id: str, name: str, value: str):
        self.value = value
        self.name = name
        self.id = id

    def to_html(self):
        return f"<input id='{self.id}' name='{self.name}' value='{self.value}' />"
