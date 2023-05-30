f=open('Đề 3/Bài 4 Kiến tha mồi/antmeet.inp')
g=open('Đề 3/Bài 4 Kiến tha mồi/antmeet.out','w')

def cmpx(ant):
    return ant[1]
def cmpd(ant):
    return -ant[2],ant[1]
def sumweight(dir,Le,Ri):
    weight=0
    if dir==1:
        weight=a[Ri][0]
        Ri-=1
    else:
        weight=a[Le][0]
        Le+=1
def posbinsearch(l,r,t,x):
    pos=n
    while 1<=r:
        mid=(l+r)//2
        if a[mid][1]-t<x+t:
            l=mid+1
        else:
            pos=mid
            r=mid-1
    return pos

n,L=map(int,f.readline().split())
a=[]
b=[]
sumw=0
T=0
res=0
for i in range (n):
    w,x,d=map(int,f.readline().split())
    a.append((w,x,d))
    if d==1:
        x=L-x
    b.append((w,x,d))
    sumw+=w

a.sort(key=cmpx)
a=[(0,0,0)]+a
b.sort(key=cmpx)
b=[(0,0,0)]+b+[(0,0,0)]
w=0
left=1
right=n
i=1
while i<=n:
    wi,left,right=sumweight(b[i][2],left,right)
    w+=wi
    if b[i][1]==b[i+1][1]:
        i+=1
        wi,left,right=sumweight(b[i][2],left,right)
        w+=wi
    T=b[i][1]
    if w>=sumw/2:
        break
    i+=1

a.remove((0,0,0))
a.sort(key=cmpd)
a=[(0,0,0)]+a
for i in range (1,n+1):
    if a[i][2]==-1:
        right=i-1
        break
for i in range (1,right+1):
    fipos=posbinsearch(right+1,n,0,a[i][1])
    scpos=posbinsearch(right+1,n,T,a[i][1])
    res+=scpos-fipos+1
print(res,file=g)
f.close()
g.close()