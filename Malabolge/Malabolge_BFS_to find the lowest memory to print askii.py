from collections import deque
crazy=(
    (1,0,0),
    (1,0,2),
    (2,2,1)
)
def thr(ti):
    tn=3
    ts=''
    tq=1
    while tq!=0:
        tq,tp=divmod(ti,tn)
        ti=tq
        ts=str(tp)+ts
    return int(ts)


def crz(ca,cb):
    ca3,cb3=str(thr(ca)),str(thr(cb))
    ca3,cb3='0'*(10-len(ca3))+ca3,'0'*(10-len(cb3))+cb3
    cr=''
    for i in range(10):
        cr+=str(crazy[int(ca3[i])][int(cb3[i])])
    return int(cr,3)

a=40
code=[list(range(33,127))]*94

visited=[False]*94*94

def bfs(v):
    a=40
    q=deque()
    q.append(v)
    while q:
        x=q.popleft()
        print(crz(x,a))
        a=crz(x,a)
        for i in code[x]:
            if not visited[i]:
                q.append(i)
                visited[i]=True
bfs(33)
