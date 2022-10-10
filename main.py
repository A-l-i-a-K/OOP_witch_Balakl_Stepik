import re

# pattern = input()
string = input()



def cleanhtml(raw_html):
  cleantext = re.sub(r'<.*?>', '', raw_html)
  return cleantext

res = cleanhtml(string)
res  = re.sub(' ','', res)

for el in res:
    if el != '':
        for s in el:
            print(s, end=' ')

