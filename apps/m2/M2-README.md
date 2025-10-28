# Milestone 2

This document lists all BeautifulSoup API functions and classes used in Milestone 1 and Part-1 of Milestone 2. File names and line numbers refer to the original source code (`beautifulsoup.zip`) before any modifications.

| API / Class | File | Line number | Description |
|-------------|------|------------|-------------|
| BeautifulSoup() | __init__.py | 133 | A data structure representing a parsed HTML or XML document |
| find_all() | element.py | 2715 | Look in the children of this `PageElement` and find all `PageElement` objects that match the given criteria |
| find_parent() | element.py | 992 | Find the closest parent of this PageElement that matches the given criteria |
| find_next() | element.py | 747 | Find the first PageElement that matches the given criteria and appears later in the document than this PageElement |
| get_text() | element.py | 524 | Get all child strings of this PageElement, concatenated using the given separator |
| prettify() | element.py | 2601 | Pretty-print this `Tag` as a string or bytestring |
| SoupStrainer() | filter.py | 313 | The `ElementFilter` subclass used internally by Beautiful Soup |