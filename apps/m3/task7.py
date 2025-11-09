from bs4 import BeautifulSoup
from bs4.soupreplacer import SoupReplacer
import sys

input_file = sys.argv[1]
output_file = "task7_" + input_file

# read the file
with open(input_file, "r", encoding="utf-8") as f:
    content = f.read()

# define xformer function to set class="test" on all <p> tags
def set_p_class(tag):
    if tag.name == "p":
        tag.attrs["class"] = ["test"]

# create a SoupReplacer using the xformer
replacer = SoupReplacer(xformer=set_p_class)

# parse HTML with the replacer
soup = BeautifulSoup(content, "html.parser", replacer=replacer)

# write the modified tree to a file
with open(output_file, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"All <p> tags now have class='test' and saved to {output_file}")
