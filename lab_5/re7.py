import re
with open ('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
pattern = ('([a-z]+)(_)([a-z]+)')
text1 = re.search(pattern, text).group(1)
text2 = re.search(pattern, text).group(3)
text2 = text2.capitalize()
text = text1 + text2
print(text)


# import re

# pattern = r"(.*?)_([a-zA-Z])"

# def camel(match):
#     return match.group(1) + match.group(2).upper()

# def camel_upper(match):
#     return match.group(1)[0].upper() + match.group(1)[1:] + match.group(2).upper()

# words = """add
# matrix_add
# diagonal_matrix_add
# pseudo_inverse""".splitlines()

# results = [re.sub(pattern, camel, w, 0) for w in words]
# print(results)