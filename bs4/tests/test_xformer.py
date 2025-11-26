import pytest
from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

class TestSoupReplacer:

    def test_og_tag_replacement(self):
        html = "<b>hello</b>"
        replacer = SoupReplacer(og_tag="b", alt_tag="strong")
        if "<b>" in html:
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        assert soup.find("b") is None
        assert soup.find("strong") is not None
        assert soup.find("strong").text == "hello"

    def test_name_xformer(self):
        html = "<i>italic text</i>"
        replacer = SoupReplacer(name_xformer=lambda tag: "em" if tag.name == "i" else tag.name)
        if "<i>" in html:
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        assert soup.find("i") is None
        assert soup.find("em") is not None
        assert soup.find("em").text == "italic text"

    def test_attrs_xformer(self):
        html = '<p class="foo" id="bar">text</p>'
        def remove_class(tag):
            return {k:v for k,v in tag.attrs.items() if k != "class"}
        replacer = SoupReplacer(attrs_xformer=remove_class)
        if html.strip():
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        p_tag = soup.find("p")
        assert "class" not in p_tag.attrs
        assert p_tag.attrs["id"] == "bar"
        assert p_tag.text == "text"

    def test_xformer_side_effect(self):
        html = "<div>content</div>"
        def add_data_attr(tag):
            tag.attrs["data-added"] = "true"
        replacer = SoupReplacer(xformer=add_data_attr)
        if html.strip():
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        div_tag = soup.find("div")
        assert div_tag.attrs.get("data-added") == "true"
        assert div_tag.text == "content"

    def test_combined_transformers(self):
        html = '<span class="old">hi</span>'
        replacer = SoupReplacer(
            name_xformer=lambda tag: "div",
            attrs_xformer=lambda tag: {"class": "new"},
            xformer=lambda tag: tag.attrs.update({"data-checked": "yes"})
        )
        if html.strip():
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        div_tag = soup.find("div")
        assert div_tag is not None
        assert div_tag.attrs["class"] == "new"
        assert div_tag.attrs["data-checked"] == "yes"
        assert div_tag.text == "hi"

    def test_multiple_name_replacements(self):
        html = '<b>bold</b><i>italic</i>'
        replacer = SoupReplacer(
            name_xformer=lambda tag: "strong" if tag.name=="b" else ("em" if tag.name=="i" else tag.name)
        )
        if html.strip():
            soup = BeautifulSoup(html, "html.parser", replacer=replacer)
        else:
            soup = html
        assert soup.find("b") is None
        assert soup.find("i") is None
        strong_tag = soup.find("strong")
        em_tag = soup.find("em")
        assert strong_tag is not None and strong_tag.text == "bold"
        assert em_tag is not None and em_tag.text == "italic"
