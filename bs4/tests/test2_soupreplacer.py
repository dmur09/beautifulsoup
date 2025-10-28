from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

# Create a replacer to swap <b> tags with <blockquote> tags
replacer = SoupReplacer("b", "blockquote")

# Sample HTML with multiple <b> tags, including nested ones
html2 = "<div><b>One</b><b>Two</b><p><b>Nested</b></p></div>"

# Parse the HTML with the replacer
soup2 = BeautifulSoup(html2, "html.parser", replacer=replacer)

# Check that no <b> tags remain
assert not soup2.find_all("b"), "All <b> tags should be replaced"

# Check that all <b> tags were correctly replaced by <blockquote>
blockquotes = soup2.find_all("blockquote")
assert len(blockquotes) == 3, "There should be three <blockquote> tags"

# Verify that the nested <b> tag was replaced correctly
assert blockquotes[2].text == "Nested", "Nested <b> tag should be replaced correctly"

print("Test case 2 passed!")
