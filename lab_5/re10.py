import re
with open('row.txt', 'r', encoding= 'utf-8') as file:
    text = file.read()
pattern = r'(?<!^)(?=[A-Z])'
name = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
print(name)