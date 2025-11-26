import pytest
from bs4 import BeautifulSoup

class TestDFSIterable:
    def _collect_nodes(self, node):
        """Helper function to collect node types and names for assertions using DFS iteration."""
        result = []
        if node is None:
            return result
        for n in node:  # uses the custom __iter__ (DFS)
            if hasattr(n, "name") and n.name is not None:
                result.append(f"Tag: {n.name}")
            else:
                text = str(n).strip()
                if text:
                    result.append(f"Text: {text}")
        return result

    def test_multiple_children(self):
        html = "<div><p>One</p><span>Two</span></div>"
        soup = BeautifulSoup(html, "html.parser")
        expected = [
            "Tag: [document]",
            "Tag: div",
            "Tag: p",
            "Text: One",
            "Tag: span",
            "Text: Two",
        ]
        assert self._collect_nodes(soup) == expected

    def test_empty_div(self):
        html = "<div></div>"
        soup = BeautifulSoup(html, "html.parser")
        expected = ["Tag: [document]", "Tag: div"]
        assert self._collect_nodes(soup) == expected

    def test_mixed_content(self):
        html = "<div>Hello <b>Bold</b> World</div>"
        soup = BeautifulSoup(html, "html.parser")
        expected = ["Tag: [document]", "Tag: div", "Text: Hello", "Tag: b", "Text: Bold", "Text: World"]
        assert self._collect_nodes(soup) == expected

    def test_nested_tags(self):
        html = "<div><p><b>Bold</b></p></div>"
        soup = BeautifulSoup(html, "html.parser")
        expected = ["Tag: [document]", "Tag: div", "Tag: p", "Tag: b", "Text: Bold"]
        assert self._collect_nodes(soup) == expected

    def test_full_soup_traversal(self):
        html = "<html><body><div><p>A</p><p>B</p></div></body></html>"
        soup = BeautifulSoup(html, "html.parser")
        expected = [
            "Tag: [document]",
            "Tag: html",
            "Tag: body",
            "Tag: div",
            "Tag: p",
            "Text: A",
            "Tag: p",
            "Text: B",
        ]
        assert self._collect_nodes(soup) == expected
