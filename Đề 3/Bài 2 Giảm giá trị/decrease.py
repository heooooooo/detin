f=open('Đề 3/Bài 2 Giảm giá trị/decrease.inp')
g=open('Đề 3/Bài 2 Giảm giá trị/decrease.out','w')
n=int(f.readline())
def max(n):
    n=str(n)
    max=0
    for i in n:
        if int(i)>max:
            max=int(i)
    return max
res=0
while n>0:
    n-=max(n)
    res+=1
print(res,file=g)
f.close()
g.close()
