import re

text = "I like to eat apples. Apple are my favorite fruit."
new_text = re.sub(r'\b[Aa]pples?\b', 'Oranges', text)
print(new_text)