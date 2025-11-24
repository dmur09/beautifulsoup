# Milestone-4

**Overview**  
Iterable BeautifulSoup is a version of BeautifulSoup that lets you go through HTML or XML documents one piece at a time, making it easier to work with large files.

**Key Features**  
- Go through tags, text, and attributes using a loop  
- Works with large documents without using too much memory  
- Can be used with Python generators or async code  
- Compatible with normal BeautifulSoup objects

**Example**  
```python
from bs4 import IterableSoup

for node in IterableSoup(html_doc):
    if node.name == "a":
        print(node.get("href"))