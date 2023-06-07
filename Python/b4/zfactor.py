f=open('b4/zfactor.inp')
g=open('b4/zfactor.out','w')

def pt(x):
    i=2
    a=[]
    while x>1:
        if x%i==0:
            a.append(i)
            x=x/i
        else:
            i+=1
    if len(a)==0:
        a.append(x)
    return a

n,k=map(int,f.readline().split())
a=list(map(int,f.readline().strip().split()))
b=[]
for i in range (2,k+1):
    b.append(min(pt(i)))
out=[]
count=0
for i in a:
    for j in b:
        if j==i:
            count+=1
    out.append(count)
    count=0
for i in out:
    print(i,file=g)

f.close()
g.close()