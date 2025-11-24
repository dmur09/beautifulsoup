# Milestone-4

**Overview**  
Iterable BeautifulSoup extends the standard BeautifulSoup library to enable Pythonic iteration over HTML/XML documents, improving memory efficiency and traversal simplicity.

**Problem**  
Traditional BeautifulSoup builds full parse trees and relies on search methods (`find_all`), which can be inefficient for large or streaming documents.

**Key Features**  
- **Node Iteration API:** Iterate over tags, strings, and attributes in document order.  
- **Streaming-Friendly:** Process documents incrementally without full tree materialization.  
- **Functional Utilities:** Support `map`, `filter`, and generator-based transformations.  
- **Async Support (Optional):** `async for` traversal for asynchronous pipelines.  
- **Backwards Compatibility:** Works with standard BeautifulSoup objects.

**Example Usage**  
```python
from bs4 import IterableSoup

for node in IterableSoup(html_doc):
    if node.name == "a":
        print(node.get("href"))

