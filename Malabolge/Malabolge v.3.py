# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 09:43:46 2024

@author: user
"""

pow9,pow10=3**9,3**10
code=list("X"*94);code[4]="J";code[5]="P";code[23]="I";code[39]="R";code[40]="M";code[62]="C";code[68]="N";code[81]="E"
crz_crt=(
       (1,0,0),
       (1,0,2),
       (2,2,1)
)

def crz(a,b):
    d=1
    s=0
    
    for i in range(10):
        s+=crz_crt[(a//d)%3][(b//d)%3]*d
        d*=3
        
    return s

def rotr(i):
    return (i%3)*pow9+(i//3)

encr_crt=list(map(ord,"9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@5z]&gqtyfr$(we4{WP)H-Zn,[%\\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb"))

def encp(c):
    return encr_crt[c%94]

def main(inp):
    memory=[0]*pow10
    a=0
    c=0
    d=0
    n=0
    k=0
    ptr=''
    for i in range(len(inp)):
        memory[i]=ord(inp[i])

    if len(inp)>pow10:
        print("LengthError")
        return 0
    print("LengthError checked")
    for s in range(len(inp)):
        if memory[s]<33 or memory[s]>127:
            print("SyntaxError",memory[s])
            return 0
    print("SyntaxError checked")

    for i in range(len(inp),pow10):
        memory[i]=memory[i-1]+memory[i-2]

    print("start")
    while 1:
        n=(c+memory[c]-k)%94
        print(f"{c-k:>3}:{code[n]},{k} [{memory[c]}] n={n:>5}/{chr(memory[c]):>2}|a={a:>5}, c={c-k:>3}, d={d:>5}, [c]={memory[c]:>5}, [d]={memory[d]:>5} | print : '{ptr}' ")
        if memory[c]<33 or memory[c]>126:
            print("X poped",c,chr(memory[c]))
            k+=1
            continue

        if n==4:
           c=memory[d]%pow10-k
        elif n==5:
            ptr+=chr(a%256)
        elif n==23:
            print("read:>",end='')
            a=ord(input()[0])
        elif n==39:
            a=memory[d]=rotr(memory[d])%pow10
        elif n==40:
            d=memory[d]%pow10
        elif n==62:
            a=memory[d]=crz(memory[d],a)%pow10
        elif n==68:
            pass
        elif n==81:
            break
        else:
            if c==0:
                print("TextFrror")
                break
            k+=1
        print(f"                        |a={a:>5}, c={c-k:>3}, d={d:>5}, [c]={memory[c]:>5}, [d]={memory[d]:>5}")
        
        if memory[c]>=33 and memory[c]<=126:
            memory[c]=encp(memory[c])

        c=(c+1)%pow10 if c<pow10 else 0
        d=(d+1)%pow10 if d<pow10 else 0

    for i in range(len(inp)):
        print(chr(memory[i]),end="")
    print("\n")
    print(ptr)

if __name__=="__main__":
    inp=' '
    s=''
    print("THIS IS MALABOLGE v.3\nWRITE DOWN YOUR CODE.")
    while inp!='':
        inp=input()
        s+=inp
    main(s)


"""
(=<`:9876Z4321UT.-Q+*)M'&%$H"!~}|Bzy?=|
{z]KwZY44Eq0/{mlk**hKs_dG5[m_BA{?-
Y;;Vb'rR5431M}/.zHGwEDCBA@98\6543W10/.R,+O<
"""

"""
(=<`$9]7<5YXz7wT.3,+O/o'K%$H"'~D|#z`{^Lx8%$Xmrkophm-kNi;gsedcba`_^]\{ZYXWVUTSRQPONMLKJIHGFEDCBA?>=<;:9876543s+O<oLm
"""
"""
D'`N
@p8~[5X9Vx6v4tc>=p(nnmHjF'3VUd"@~,=^):rqvutsl2Sinmlkjiba'_
dcbaZ~A@\
UTx;WPUTMqQ3ONGkE-CHA@d>CBA@9]=6|:32V65.32+0/o-
&Jk)"!&}C3"!a}|u;yxZvo%srkpomf,jihgfH%}\
[`_XW{>=YXQuN6LpJONMFjJ,BAFEDCB;_?>=6|:32V0/SRQ>
"""
