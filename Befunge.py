from random import randint as r

easter=input("THIS BEFUNGE 98. \nPRESS ENTER.")
if easter=='admin':
    ad=1
else:
    ad=0
s=' '
code=[]
while s!='':
    s=input()
    code.append(list(s))
code.pop()
m=[]
dx=dy=0
px=py=0
c=list('0123456789+-/%!`><^v?_|":\\$.,#gp&~@')
while 1:
    s=code[dx][dy]
    if ad==1:
        print(dx,dy,s,'#'*5,*m)
    for i in range(10):
        if s==str(i):
            m.append(i)
    if s=='+':
        a,b=m.pop(),m.pop()
        m.append(a+b)
    elif s=='-':
        a,b=m.pop(),m.pop()
        m.append(b-a)
    elif s=='/':
        a,b=m.pop(),m.pop()
        if a==0:
            m.append(int(input()))
        else:
            m.append(b//a)
    elif s=='%':
        a,b=m.pop(),m.pop()
        if a==0:
            m.append(int(input()))
        else:
            m.append(b%a)
    elif s=='!':
        if m.pop()==0:
            m.append(1)
        else:
            m.append(0)
    elif s=='`':
        a,b=m.pop(),m.pop()
        if b>a:
            m.append(1)
        else:
            m.append(0)
    elif s=='^':
        px=-1
        py=0
    elif s=='v':
        px=1
        py=0
    elif s=='<':
        px=0
        py=-1
    elif s=='>':
        px=0
        py=1
    elif s=='?':
        px=r(-1,1)
        if px==0:
            py=r(-1,1)
            while py==0:
                py=r(-1,1)
        else:
            py=0
    elif s=='_':
        px=0
        if m.pop()==0:
            py=1
        else:
            py=-1
    elif s=='|':
        py=0
        if m.pop()==0:
            px=1
        else:
            px=-1
    elif s=='"':
        dx+=px
        dy+=py
        s=code[dx][dy]
        while s!='"':
            m.append(ord(s))
            dx+=px
            dy+=py
            s=code[dx][dy]
    elif s==':':
        m.append(m[-1])
    elif s=='\\':
        a,b=m.pop(),m.pop()
        m.append(b,a)
    elif s=='$':
        m.pop()
    elif s=='.':
        if ad==1:
            print('>'*20, m.pop())
        else:
            print(m.pop(),end=' ')
    elif s==',':
        if ad==1:
            print('>'*20, chr(m.pop()))
        else:
            print(chr(m.pop()),end='')
    elif s=='#':
        dx+=px
        dy+=py
        s=code[dx][dy]
        while not s in c:
            dx+=px
            dy+=py
            s=code[dx][dy]
    elif s=='g':
        y,x=m.pop(),m.pop()
        m.append(ord(code[x][y]))
    elif s=='p':
        y,x,v=m.pop(),m.pop(),m.pop()
        code[x][y]=chr(v)
    elif s=='&':
        while 1:
            try:
                a=int(input("INPUT NUMBER >>>"))
                break
            except:
                pass
        m.append(a)
    elif s=='~':
        m.append(ord(input("INPUT TEXT >>>")))
    elif s=='@':
        break
    dx+=px
    dy+=py


"""
vv  <      <
    2       
    ^  v<   
 v1<?>3v4   
    ^   ^   
>   ?>  ?>5^
    v   v   
 v9<?>7v6   
    v  v<   
    8       
 .  >  >   ^
^<          
"""

'''
>"!dlrow ,olleH",,,,,,,,,,,,,@
'''

'''
>&&+.@
'''

'''
v.<<<<<<<<
 >^2       
  1^3      
  ^?^ 4   
   ^ 6^5  
>  ?> ?^  
 9 v ^<   
 ^<?>7  ^  
   >8  > ^
'''
