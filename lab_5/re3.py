import re
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'[[a-z]+]([a-z]_[a-z])([a-z]+)'
ab = re.findall(pattern, text)
print(ab)