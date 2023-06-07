f=open('b2/cost.inp')
g=open('b2/cost.out','w')

n,a,b=map(int,f.readline().split())
arr=list(map(int,f.readline().strip().split()))
if a>b:
    a,b=b,a
res=0
for i in arr:
    if i==2:
        res+=a+b
    else:
        res+=a
print(res,file=g)
f.close()
g.close()
