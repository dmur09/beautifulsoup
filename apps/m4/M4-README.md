## Milestone-4

## Technical Brief

We made `BeautifulSoup` iterable by adding a DFS-based `__iter__` method to the `Tag` class in `element.py`. This allows users to write:

```python
for node in soup:
    print(node)
```

# Design Summary

Implemented __iter__ and a recursive _dfs generator inside Tag.

DFS yields each node one at a time—no list building, satisfying the milestone requirement.

Because BeautifulSoup inherits from Tag, the whole soup becomes iterable automatically.

# Why This Design

Efficient: generator-based traversal uses minimal memory.

Simple: works for all tags and the root soup object.

Matches natural HTML structure traversal (top-down, left-to-right).