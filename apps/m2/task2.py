from bs4 import BeautifulSoup, SoupStrainer
import sys

# Open the HTML file specified as the first command-line argument
with open(sys.argv[1], "r", encoding="utf-8") as f:
    html_doc = f.read()

# Only parse <a> tags from the HTML
only_a_tags = SoupStrainer("a")
soup = BeautifulSoup(html_doc, "html.parser", parse_only=only_a_tags)

# Print the href attribute of each <a> tag
for link in soup.find_all("a"):
    print(link.get("href"))
