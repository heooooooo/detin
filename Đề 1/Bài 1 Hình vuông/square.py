f=open('Đề 1/Bài 1 Hình vuông/square.inp')
g=open('Đề 1/Bài 1 Hình vuông/square.out','w')
n=int(f.readline())
x=[0]*n
y=[0]*n
for i in range (n):
    x[i],y[i]=map(int,f.readline().split())
xmax=max(x)
xmin=min(x)
ymax=max(y)
ymin=min(y)
c=max(xmax-xmin,ymax-ymin)
print(c*c,file=g)
f.close()
g.close()