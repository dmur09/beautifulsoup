from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

html1 = "<b>hello</b>"
replacer1 = SoupReplacer(og_tag="b", alt_tag="strong")
soup1 = BeautifulSoup(html1, "html.parser", replacer=replacer1)
print(soup1)

html2 = "<i>italic text</i>"
replacer2 = SoupReplacer(name_xformer=lambda tag: "em" if tag.name == "i" else tag.name)
soup2 = BeautifulSoup(html2, "html.parser", replacer=replacer2)
print(soup2)

html3 = '<p class="foo" id="bar">text</p>'
def remove_class(tag):
    return {k:v for k,v in tag.attrs.items() if k != "class"}
replacer3 = SoupReplacer(attrs_xformer=remove_class)
soup3 = BeautifulSoup(html3, "html.parser", replacer=replacer3)
print(soup3)

html4 = "<div>content</div>"
def add_data_attr(tag):
    tag.attrs["data-added"] = "true"
replacer4 = SoupReplacer(xformer=add_data_attr)
soup4 = BeautifulSoup(html4, "html.parser", replacer=replacer4)
print(soup4)

html5 = '<span class="old">hi</span>'
replacer5 = SoupReplacer(
    name_xformer=lambda tag: "div",
    attrs_xformer=lambda tag: {"class": "new"},
    xformer=lambda tag: tag.attrs.update({"data-checked": "yes"})
)
soup5 = BeautifulSoup(html5, "html.parser", replacer=replacer5)
print(soup5)

html6 = '<b>bold</b><i>italic</i>'
replacer6 = SoupReplacer(
    name_xformer=lambda tag: "strong" if tag.name=="b" else ("em" if tag.name=="i" else tag.name)
)
soup6 = BeautifulSoup(html6, "html.parser", replacer=replacer6)
print(soup6)