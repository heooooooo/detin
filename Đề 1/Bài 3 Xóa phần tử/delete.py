f=open('Đề 1/Bài 3 Xóa phần tử/delete.inp')
g=open('Đề 1/Bài 3 Xóa phần tử/delete.out','w')
n=int(f.readline())
a=list(map(int,f.readline().strip().split()))
base=10**9+7
a=[0]+a
cnum1=[0]*(n+1)
cnum3=[0]*(n+2)
for i in range (1,n+1):
    if (a[i]==1):
        cnum1[i]=cnum1[i-1]+1
    else:
        cnum1[i]=cnum1[i-1]
for i in range(n,0,-1):
    if (a[i]==3):
        cnum3[i]=cnum3[i+1]+1
    else:
        cnum3[i]=cnum3[i+1]
pos2=0
res=0
for i in range(1,n+1):
    if (a[i]==2):
        cnum1[i]+=cnum1[pos2]
        res= (res+(cnum1[i]*cnum3[i]) % base) % base
        cnum1[i]+=cnum1[pos2]
        pos2=i
print(res,file=g)
f.close()
g.close()