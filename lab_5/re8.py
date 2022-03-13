import re
text = 'ErlanulyTemirlan'
print(re.findall('[A-Z][^A-Z]*', text))