# Milestone-4

**Overview**  
Iterable BeautifulSoup extends BeautifulSoup by adding a **DFS-based iterator** to tags. This allows looping over all elements and text in depth-first order using a standard Python `for` loop.

**Key Idea**  
- `__iter__` yields the node itself and recursively all children via `_dfs_traversal`  
- Handles nested and mixed content automatically  
- Integrated into the module, so imported tags are iterable out of the box

**Example Usage**
```python
from bs4 import BeautifulSoup  # your module imports element.py

html = "<div>Hello <b>Bold</b> World</div>"
soup = BeautifulSoup(html, "html.parser")

# Iterate all elements and text (DFS order)
for node in soup.div:
    print(node.name if node.name else str(node))
# Output: div, Hello , b, Bold,  World
