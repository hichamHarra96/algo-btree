def recherchDicho(e,l):
    a=0
    b=len(l)-1
    while a<=b:
        m=(a+b)//2
        if l[m] ==e:
            return True
        elif l[m]<e:
            a=m+1
        else:
            b=m-1
    return False
