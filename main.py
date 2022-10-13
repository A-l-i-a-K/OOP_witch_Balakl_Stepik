import re

text = input()
pat = re.compile(r'''(?x)
(?P<prot>https?)://
(?P<dom>(?:[a-zA-Z\d_]+\.){1,}[a-z]+)/
[a-zA-Z\d_/\-&]*    # всё, что между доменом и параметрами
(?P<params>\?[a-zA-Z=\d_\-&]+)?
(?P<anc>\#[a-zA-Z_\d\-&]+)?''')

urls = re.finditer(pat, text)

for u in urls:
    print(f"""Полная ссылка: {u.group(0)}
Протокол: {u.group('prot')} | Домен: {u.group('dom')} | Параметры: {u.group('params')} | Якорь: {u.group('anc')}\n""")