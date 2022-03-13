import re
with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = r'(.*)([A-Z])([a-z]+)([A-Z])([a-z]+)'
text1 = re.search(pattern, text).group(2)
text2 = re.search(pattern, text).group(3)
text3 = text1 + text2
rex = re.search(pattern, text).group(4)
rex2 = re.search(pattern, text).group(5)
rex3 = rex + rex2
text3 = text3 + ' ' + rex3
print(text3)

# words = re.findall('[A-Z][a-z]*', text)