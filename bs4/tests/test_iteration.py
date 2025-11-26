from bs4 import BeautifulSoup

def print_nodes(node):
    """Helper to print tag names or text from a node using DFS traversal."""
    for n in node.depth_first():
        if hasattr(n, "name") and n.name is not None:
            print(f"Tag: {n.name}")
        else:
            text = str(n).strip()
            if text:
                print(f"Text: {text}")

# test multiple children
print("Test 1: Multiple children")
html = "<div><p>One</p><span>Two</span></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n")

# test empty div
print("Test 2: Empty div")
html = "<div></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n")

# test mixed content
print("Test 3: Mixed content")
html = "<div>Hello <b>Bold</b> World</div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n")

# test nested tags
print("Test 4: Nested tags")
html = "<div><p><b>Bold</b></p></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n")

# test root-level soup DFS
print("Test 5: Full soup traversal")
html = "<html><body><div><p>A</p><p>B</p></div></body></html>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup)
print("\n")
