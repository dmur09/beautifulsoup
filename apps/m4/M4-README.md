## Milestone-4 - Technical Brief

We made `BeautifulSoup` iterable by adding a DFS-based `__iter__` method to the `Tag` class in `element.py`. Iteration over the soup traverses the HTML tree top-down, left-to-right, yielding one node at a time:

```python
for node in soup:
    print(node)
```

# Design Summary

Implemented __iter__ and a recursive _dfs generator inside Tag.

DFS yields each node individually—no list is built, satisfying the milestone requirement.

Iterating over BeautifulSoup delegates to the root tag, so the whole document is traversed automatically.

# Why This Design

Efficient: generator-based traversal uses minimal memory.

Simple: works for all tags, nested structures, and mixed content.

Matches natural HTML structure traversal (top-down, left-to-right).