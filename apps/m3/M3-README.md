# Milestone-3

## Overview
Milestone 3 extends the `SoupReplacer` API to support **powerful functional transformations** during parsing in BeautifulSoup. Unlike Milestone 2’s simple tag name replacement, this version allows dynamic modifications of tag names, attributes, and the tag object itself.

---

## Features

- **Functional Transformers**
  - `name_xformer(tag)` → returns a new tag name  
  - `attrs_xformer(tag)` → returns a new dictionary of attributes  
  - `xformer(tag)` → directly mutates the tag (side effects allowed)  

- **Backward compatibility** with Milestone 2 string-based replacements (`og_tag` → `alt_tag`).

---

# Technical Brief

The `SoupReplacer` API in **Milestone 2** provided a simple mechanism to replace specific tag names (`og_tag` → `alt_tag`) during parsing. While this works for straightforward substitutions, it is **limited**:

- Cannot modify attributes or perform complex transformations.
- Transformations are limited to one-to-one tag replacements.

**Milestone 3** API on the other hand adds some key features:

- `name_xformer(tag)` – dynamically modifies tag names.  
- `attrs_xformer(tag)` – dynamically modifies attributes.  
- `xformer(tag)` – can perform extra mutations on the tag.

This allows much more flexible and detailed control over tag transformation during parsing. Key improvements:

- Multiple transformations can occur in one pass: rename tags, modify attributes, and apply arbitrary logic.  
- The original Milestone 2 string replacement still works, so existing use cases are preserved.

Thus, for a potential BeautifulSoup extension, I would recommend adopting the **Milestone 3 API design**. This design balances **simplicity for basic use cases** with **power and flexibility for advanced transformations**, making it a strong candidate for inclusion in a future BeautifulSoup release.

---

# Compilation

## Test Cases
```python
python test_xformer.py
```


## Task 7
```python
python task7.py input_file.html
```