def test(a,b,*args,**kwargs):
    print(a,b,args,kwargs)

import dis
def f(a):
    b = a
    return b

dis.dis(f)