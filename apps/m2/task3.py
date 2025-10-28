from bs4 import BeautifulSoup, SoupStrainer
import sys

# Open the HTML file specified as the first command-line argument
with open(sys.argv[1], "r", encoding="utf-8") as f:
    html_doc = f.read()

# Parse all tags from the HTML
all_tags_strainer = SoupStrainer(True)
soup = BeautifulSoup(html_doc, "html.parser", parse_only=all_tags_strainer)

# Print the name of each tag in the HTML
for tag in soup.find_all(True):
    print(tag.name)
