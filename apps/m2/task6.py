from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer

# Create a replacer to swap <b> tags with <blockquote> tags
b_to_blockquote = SoupReplacer("b", "blockquote")

# Read the HTML file
with open("large_test_file.html", "r", encoding="utf-8") as f:
    html_doc = f.read()

# Parse the HTML and automatically replace <b> with <blockquote>
soup = BeautifulSoup(html_doc, "html.parser", replacer=b_to_blockquote)

# Write the modified HTML to a new output file
with open("task6_output_file.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())
