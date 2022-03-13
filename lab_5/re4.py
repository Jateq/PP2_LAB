import re
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'.*[A-Z][a-z].*'
ab = re.findall(pattern, text)
print(ab)