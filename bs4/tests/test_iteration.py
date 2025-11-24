from bs4 import BeautifulSoup

print("Running DFS Iterable Tests...\n")

def print_nodes(node):
    """Helper to print tag names or text from a node using DFS iterable."""
    for n in node:
        if n.name:
            print(f"Tag: {n.name}")
        else:
            text = str(n).strip()
            if text:
                print(f"Text: {text}")

# test 1: Multiple children
print("Test 1: Multiple children")
html = "<div><p>One</p><span>Two</span></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n" + "-"*40 + "\n")

# test 2: Empty div
print("Test 2: Empty div")
html = "<div></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n" + "-"*40 + "\n")

# test 3: Mixed content
print("Test 3: Mixed content")
html = "<div>Hello <b>Bold</b> World</div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n" + "-"*40 + "\n")

# test 4: Nested tags
print("Test 4: Nested tags")
html = "<div><p><b>Bold</b></p></div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n" + "-"*40 + "\n")

# test 5: Mixed content with multiple children
print("Test 5: Mixed content with multiple children")
html = "<div>Hello <b>Bold</b> World</div>"
soup = BeautifulSoup(html, "html.parser")
print_nodes(soup.div)
print("\n" + "-"*40 + "\n")

print("DFS iterable tests completed!")
