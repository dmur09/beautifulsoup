from bs4 import BeautifulSoup

print("Running Iteration Tests...")

# Test 1: Multiple children
html = "<div><p>One</p><span>Two</span></div>"
soup = BeautifulSoup(html, "html.parser")
# FIX: Check 'if t.name' instead of 'hasattr' so None values go to the else block
tags = [t.name if t.name else str(t) for t in list(soup)[1:]] 
assert tags == ["div", "p", "One", "span", "Two"], f"Test 1 failed. Got: {tags}"

# Test 2: Empty div
html = "<div></div>"
soup = BeautifulSoup(html, "html.parser")
tags = [t.name if t.name else str(t) for t in list(soup.div)[1:]]
assert tags == [], f"Test 2 failed. Got: {tags}"

# Test 3: Text only
html = "<div>Hello world</div>"
soup = BeautifulSoup(html, "html.parser")
tags = [t.name if t.name else str(t) for t in list(soup.div)[1:]]
assert tags == ["Hello world"], f"Test 3 failed. Got: {tags}"

# Test 4: Nested tags
html = "<div><p><b>Bold</b></p></div>"
soup = BeautifulSoup(html, "html.parser")
tags = [t.name if t.name else str(t) for t in list(soup.div)[1:]]
assert tags == ["p", "b", "Bold"], f"Test 4 failed. Got: {tags}"

# Test 5: Mixed content
html = "<div>Hello <b>Bold</b> World</div>"
soup = BeautifulSoup(html, "html.parser")
tags = [t.name if t.name else str(t) for t in list(soup.div)[1:]]
assert tags == ["Hello ", "b", "Bold", " World"], f"Test 5 failed. Got: {tags}"

print("All 5 iteration tests passed!")