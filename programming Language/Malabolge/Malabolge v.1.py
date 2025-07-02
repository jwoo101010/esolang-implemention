"""
malabolge
2024-09-21 14:14:29
"""
code=[] # input code
s="" # input
i=0 # range
a=0
c=0
pc=0 # pointer c [c]
n=0 # ([c]+c)%94
d=0
pd=0 # pointer d [d]
pow10=pow(3,10) # 3¹⁰ = 59049
memory=[0]*pow10 # input code
w="" # real time
v="" # compiling code
# function to calculate
def crz(ca,cb): # a,b is string
    crazy=[
        (1,0,0),
        (1,0,2),
        (2,2,1)
    ]
    cs=""
    for i in range(max(len(ca),len(cb))):
        cs+=str(crazy[int(ca[i])][int(cb[i])])
    return cs
def rotr(rs): # rotate last num to first, rs:string
    return rs[-1]+rs[1:-1]
def tri(ti): # tri-num(삼진법) ti:int
    tj=ti
    tq=tr=1
    ts=""
    while tq!=0:
        tq,tr=divmod(tj,3)
        ts=str(tr)+ts
        tj=tq
    return "0"*(10-len(ts))+ts
def encode(es): # encode for code  es:pc=>[c]
    em=list("9m<.TVac`uY*MK'X~xDl}REokN:#?G\"i@5z]&gqtyfr$(we4{WP)H-Zn,[%\3dL+Q;>U!pJS72FhOA1CB6v^=I_0/8|jsb")
    return em[es%94]
# function end
print("THIS IS MALABOLGE.\nWRITE YOUR CODE.")
# input code
while 1:
    s=input()
    if s=="":
        break
    for i in s:
        code.append(i)
    code.append("\n")
# send to memory
for i in range(len(code)):
    memory[i]=tri(ord(code[i]))
# fill the memory
for i in range(len(code),len(memory)):
    memory[i]=crz(memory[i-1],memory[i-2])
# code's order start
a=0
c=0
d=0
v={
    4:"jmp [d] + 1",
    5:"out a",
    23:"in a",
    39:"rotr [d] ; mov a,[d]",
    40:"mov d,[d]",
    64:"crz [d],a ; mov a,[d]",
    68:"nop",
    81:"end"
}
while 1:
    c=int(memory[pc],3)
    d=int(memory[pd],3)
    n=(pc+c)%94
    if n==4: # jmp [d] + 1
        pc=d+1
    elif n==5: # out a
        print(chr(a))
    elif n==23: # in a
        s=input()
        if s=="":
            a=10
        elif s=="\0":
            a=pow10-1
        else:
            a=ord(s)
    elif n==39: # rotr [d] ; mov a,[d]
        pd=rotr(pd)
        a=pd
    elif n==40: # mov d,[d]
        d=pd
    elif n==64: # crz [d],a ; mov a,[d]
        pd=crz(pd,a)
        a=pd
    elif n==68: # nop
        pass
    elif n==81: # end
        break
    else:
        if pc==0:
            raise NameError
    w=chr(c)
    if w=="\n":
        w="\\n"
    try:
        print(f"{pc} => c={c}:{w} \\ num={n}|{v[n]}|a={a},d={d},[d]={pd}")
    except:
        print(f"{pc} => c={c}:{w} \\ num={n}|nop!|a={a},d={d},[d]={pd}")
    pc+=1
    pd+=1
    
