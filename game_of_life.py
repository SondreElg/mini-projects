import numpy as n,pygame as p
q=(999,)*2
b=n.empty(q,bool)
t=p.display
r=n.roll
o=p.surfarray.pixels2d(t.set_mode(q))
while 1:
 w=sum(r(r(b,a,0),c,1)for a in[-1,0,1]for c in[-1,0,1])
 b=b&((w==3)|(w==4))|((~b)*(w==3))
 o[:,:]=0-b
 t.flip()