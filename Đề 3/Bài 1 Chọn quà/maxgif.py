f=open('Đề 3/Bài 1 Chọn quà/maxgif.inp')
g=open('Đề 3/Bài 1 Chọn quà/maxgif.out','w')
n=int(f.readline())
a=list(map(int,f.readline().strip().split()))
max=0
for i in range (n-1):
    for j in range (i+1,n):
        s=a[i]+a[j]
        if s>max:
            max=s
print(max,file=g)
f.close()
g.close()