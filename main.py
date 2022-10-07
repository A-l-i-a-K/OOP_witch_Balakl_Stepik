import re

st = input() # HTML

res = re.findall(r'''<a\s[^>]+?href\s?=\s?['"]([^'"]*)['"]''', st)

print(*res, sep='\n')
