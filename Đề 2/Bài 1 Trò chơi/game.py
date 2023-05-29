f=open('Đề 2/Bài 1 Trò chơi/game.inp')
g=open('Đề 2/Bài 1 Trò chơi/game.out','w')
a,b=map(int,f.readline().split())
res=0
for i in range(2):
    if a>=b:
        res+=a
        a-=1
    else:
        res+=b
        b-=1
print(res,file=g)
f.close()
g.close()
