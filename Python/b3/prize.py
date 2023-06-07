f=open('b3/prize.inp')
g=open('b3/prize.out','w')

m,n=map(int,f.readline().split())
a=list(map(int,f.readline().strip().split()))
a.sort(reverse=True)

res1=a[m-1]*n
s=0
out=[]
for i in range (n):
    s=a[i]*(i+1)
    out.append(s)
    s=0

if res1>max(out):
    print(res1,file=g)
else:
    print(max(out),file=g)

f.close()
g.close()
