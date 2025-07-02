from pprint import pprint as pp
s=' '
code=[]
while s!='':
    s=input()
    code.append(list(s))
code.pop()
pp(code)
