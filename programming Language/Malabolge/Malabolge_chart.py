for i in range(95):
    print(i)
    for j in range(32,127):
        if (i+j)%94==4:
            jj=j
        if (i+j)%94==5:
            p=j
        if (i+j)%94==23:
            ii=j
        if (i+j)%94==39:
            r=j
        if (i+j)%94==40:
            m=j
        if (i+j)%94==62:
            c=j
        if (i+j)%94==68:
            n=j
        if (i+j)%94==81:
            e=j
    print(f"J:{chr(jj)}, P:{chr(p)}, I:{chr(ii)}, R:{chr(r)}, M:{chr(m)}, C:{chr(c)}, N:{chr(n)}, E:{chr(e)}")
