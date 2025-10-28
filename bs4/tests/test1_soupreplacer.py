from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

# Create a replacer to swap <b> tags with <blockquote> tags
replacer = SoupReplacer("b", "blockquote")

# Test that the replacer stores the correct tags
assert replacer.og_tag == "b", "Original tag should be 'b'"
assert replacer.alt_tag == "blockquote", "Replacement tag should be 'blockquote'"

# Sample HTML to test the replacement
html = "<html><body><b>Bold text</b><p>Paragraph</p></body></html>"

# Parse the HTML with the replacer
soup = BeautifulSoup(html, "html.parser", replacer=replacer)

# Verify that <b> tags are replaced by <blockquote>
assert soup.find("b") is None, "<b> tags should be replaced"
assert soup.find("blockquote") is not None, "<blockquote> should exist"

# Verify that other content remains unchanged
assert soup.find("p").text == "Paragraph", "Paragraph text should remain unchanged"

print("Test case 1 passed!")
