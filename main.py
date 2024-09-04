from elements.a import AElement
from elements.div import DivElement
from elements.form import FormElement
from elements.img import ImgElement
from elements.input import InputElement
from elements.select import SelectElement

a_element = AElement(href="https://www.seznam.cz", link_name="www.seznam.cz")
img_element = ImgElement(src="https://www.seznam.cz/image.jpg", alt="Seznam obrázek")
input_element = InputElement(id="input_name", name="input_name", value="Text")
select_element = SelectElement(id="input_name", name="input_name", options=(("1", "Volba 1"), ("2", "Volba 2")))

form = FormElement(input_element.to_html() + select_element.to_html() + a_element.to_html() + img_element.to_html())
div_element = DivElement(form.to_html())

print(div_element.to_html())
