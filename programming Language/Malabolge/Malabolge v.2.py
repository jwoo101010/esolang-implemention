"""
2024-09-27 16:27:38
Malabolge v.2
"""
"""
dialog

"""
a=c=d=0
i=0
n=0
k=0
inpi=0
inp=''
s=''
ptr=''
m=[]
pow9=3**9
pow10=3**10
crazy=(
    (1,0,0),
    (1,0,2),
    (2,2,1)
)
ens=list("9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb")
en=[]
for i in ens:
    en.append(ord(i))
code=list("X"*94)
code[4]="J"
code[5]="P"
code[23]="I"
code[39]="R"
code[40]="M"
code[62]="C"
code[68]="N"
code[81]="E"

def thr(ti):
    tn=3
    ts=''
    tq=1
    while tq!=0:
        tq,tp=divmod(ti,tn)
        ti=tq
        ts=str(tp)+ts
    return int(ts)

def rotr(rn):
    return (rn%3)*pow9+(rn//3)

def crz(ca,cb):
    ca3,cb3=str(thr(ca)),str(thr(cb))
    ca3,cb3='0'*(10-len(ca3))+ca3,'0'*(10-len(cb3))+cb3
    cr=''
    for i in range(10):
        cr+=str(crazy[int(ca3[i])][int(cb3[i])])
    return int(cr,3)

def encode(ec):
    return en[ec%94]

print("THIS IS MALABOLGE v.2.\nTYPE YOUR CODE.")
while 1:
    s=input()
    if s=='':
        break
    for i in s:
        m.append(ord(i))
    m.append(10)
if not m[0]%94 in [4,5,23,39,40,62,68,81]:
    raise NameError
for i in range(len(m),pow10):
    m.append(crz(m[i-1],m[i-2]))
c=d=0
k=0
print(c,n,chr(m[c]),"\\",a,c,d,m[c],m[d])
inp=input()
while 1:
    n=(m[c]+c)%94
    ch=chr(m[c]) if m[c]!=10 else "\\n"
    print(f"{c-k:>3}:{code[n]} n={n:>5}/{ch:>2}|a={a:>5}, c={c-k:>3}, d={d:>5}, [c]={m[c]:>5}, [d]={m[d]:>5}")
    if n==4:
        c=m[d]+1
        m[c-1]=encode(m[c-1])
        d+=1
        continue
    elif n==5:
        ptr+=chr(a)
    elif n==23:
        if len(inp)==inpi:
            a=pow10-1
        elif len(inp)<inpi:
            print("SyntaxError")
            break
        else:
            a=ord(inp[inpi])
        inpi+=1
    elif n==39: # R
        m[d]=rotr(m[d])
        a=m[d]
    elif n==40: # M
        d=m[d]
    elif n==62: # C
        m[d]=crz(m[d],a)
        a=m[d]
    elif n==68:
        pass
    elif n==81:
        break
    else:
        pass
    m[c]=encode(m[c])
    c+=1
    d+=1
"""
(=<`:9876Z4321UT.-Q+*)M'&%$H"!~}|Bzy?=|{z]KwZY44Eq0/{mlk**
hKs_dG5[m_BA{?-Y;;Vb'rR5431M}/.zHGwEDCBA@98\6543W10/.R,+O<
"""

"""
(=<`:9876Z4321UT.-Q+*)M'&%$H"!~}|Bzy?=|{z]KwZY44Eq0/{mlk**
hKs_dG5[m_BA{?-Y;;Vb'rR5431M}/.zHGwEDCBA@98\6543W10/.R,+O<
"""

"""
(=<`$9]7<5YXz7wT.3,+O/o'K%$H"'~D|#z`{^Lx8%$Xmrkophm-
kNi;gsedcba`_^]\{ZYXWVUTSRQPONMLKJIHGFEDCBA?>=<;:9876543s+O<oLm
"""
print(ptr)
"""
def crz(ca,cb):
    ca3,cb3=str(thr(ca)),str(thr(cb))
    ca3,cb3='0'*(10-len(ca3))+ca3,'0'*(10-len(cb3))+cb3
    print(ca3,cb3)
    cr=''
    for i in range(10):
        cr+=str(crazy[int(ca3[i])][int(cb3[i])])
    return int(cr,3),cr
    """
