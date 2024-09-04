from elements.html import HtmlElement


class SelectElement(HtmlElement):

    def __init__(self, id: str, name: str, options: tuple):
        self.options = options
        self.name = name
        self.id = id

    def to_html(self):
        return f"<select id='{self.id}' name='{self.name}'>{self.get_options()}</select>"

    def get_options(self):
        return "".join([f"<option id='{key}'>{value}</option>" for key, value in self.options])
