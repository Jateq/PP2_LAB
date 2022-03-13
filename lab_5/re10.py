import re
# with open('row.txt', 'r', encoding= 'utf-8') as file:
#     text = file.read()
# pattern = r'(?<!^)(?=[A-Z])'
# name = re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()
# print(name)


 
def change_case(str):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', str)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
     
str = "alikhanErlanuly"
print(change_case(str))

import re

# text = 'CamelCaseLol'
# output = camel_case_lol
# f = re.sub(r'(?!^)(?=[A-Z][a-z]+)', '_', text).lower()


# print(f)