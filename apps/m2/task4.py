from bs4 import BeautifulSoup, SoupStrainer
import sys

# Open the HTML file specified as the first command-line argument
with open(sys.argv[1], "r", encoding="utf-8") as f:
    html_doc = f.read()

# Parse only tags that have an "id" attribute
id_tags_strainer = SoupStrainer(attrs={"id": True})
soup = BeautifulSoup(html_doc, "html.parser", parse_only=id_tags_strainer)

# Print the tag name and its "id" attribute
for tag in soup.find_all(True):
    if tag.has_attr("id"):
        print(f"{tag.name} id={tag['id']}")
