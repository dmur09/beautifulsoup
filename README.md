# Extended BeautifulSoup — API Enhancements

This project is a quarter-long deep dive into API design, parsing systems, and contributing to a large existing codebase. Starting from the original BeautifulSoup 4 source, I extended the library with new programmer-facing APIs, new parsing behaviors, and improved traversal mechanisms while maintaining compatibility with the existing architecture.

## 🚀 Key Features

### SoupReplacer API
Added a new system for modifying tags *during parsing*:
- `SoupReplacer(og_tag, alt_tag)` for simple replacements  
- `name_xformer`, `attrs_xformer`, and `xformer` for dynamic tag and attribute transformations  
- Improves performance by avoiding full post-parse tree traversal

### Selective Parsing (SoupStrainer)
Examples and applications using SoupStrainer to parse only the relevant parts of large HTML/XML files, improving speed and reducing memory usage.

### Iterable BeautifulSoup
Implemented generator-based iteration over all nodes:
```python
for node in soup:
    print(node)
