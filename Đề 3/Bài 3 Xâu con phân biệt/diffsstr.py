f=open('Đề 3/Bài 3 Xâu con phân biệt/diffsstr.inp')
g=open('Đề 3/Bài 3 Xâu con phân biệt/diffsstr.out','w')
n=int(f.readline())
s=f.readline()
temp=0
res=[]
for i in range (n-1):
    for j in range (i,n):
        if s[j] not in s[i:j]:
            temp+=1
        else:
            res.append(temp)
            temp=0
print(max(res),file=g)
f.close()
g.close()
