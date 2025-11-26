from bs4 import BeautifulSoup

def print_nodes(node):
    """Helper to print tag names or text from a node using DFS traversal."""
    if node is None:
        return
    for n in node:  # directly iterate; __iter__ does DFS now
        if hasattr(n, "name") and n.name is not None:
            print(f"Tag: {n.name}")
        else:
            text = str(n).strip()
            if text:
                print(f"Text: {text}")

# test multiple children
print("Test 1: Multiple children")
html1 = "<div><p>One</p><span>Two</span></div>"
soup1 = BeautifulSoup(html1, "html.parser")
print_nodes(soup1)  # start from root
print("\n")

# test empty div
print("Test 2: Empty div")
html2 = "<div></div>"
soup2 = BeautifulSoup(html2, "html.parser")
print_nodes(soup2)
print("\n")

# test mixed content
print("Test 3: Mixed content")
html3 = "<div>Hello <b>Bold</b> World</div>"
soup3 = BeautifulSoup(html3, "html.parser")
print_nodes(soup3)
print("\n")

# test nested tags
print("Test 4: Nested tags")
html4 = "<div><p><b>Bold</b></p></div>"
soup4 = BeautifulSoup(html4, "html.parser")
print_nodes(soup4)
print("\n")

# test full soup traversal
print("Test 5: Full soup traversal")
html5 = "<html><body><div><p>A</p><p>B</p></div></body></html>"
soup5 = BeautifulSoup(html5, "html.parser")
print_nodes(soup5)
print("\n")

print("DFS iterable tests completed!")