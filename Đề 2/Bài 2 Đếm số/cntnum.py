f=open('Đề 2/Bài 2 Đếm số/cntnum.inp')
g=open('Đề 2/Bài 2 Đếm số/cntnum.out','w')
a,b,c,d=map(int,f.readline().split())
res=0
for i in range (a,b+1):
    if i%c!=0 and i%d!=0:
        res+=1
print(res,file=g)
f.close()
g.close()

