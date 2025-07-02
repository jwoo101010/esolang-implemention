s=''
c=''
code=[]
while s!='END':
    s=input()
    c+=s+'\n'
c=c[0:-5:]
print(c)
for i in c:
    if i==' ':
        code.append('S')
    elif i=='\t':
        code.append('T')
    elif i=='\n':
        code.append('L')

print(*code)
