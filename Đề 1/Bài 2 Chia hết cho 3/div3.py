f=open('Đề 1/Bài 2 Chia hết cho 3/div3.inp')
g=open('Đề 1/Bài 2 Chia hết cho 3/div3.out','w')
n=int(f.readline())
a=list(map(int,f.readline().strip().split()))
c=[0,0,0] #Đếm phân phối độ phức tạp O(n)
for x in a:
    c[x%3]+=1
res=(c[0]*(c[0]-1))//2 + c[1]*c[2]
print(res,file=g)
f.close()
g.close()