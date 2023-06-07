f=open('b1/clock.inp')
g=open('b1/clock.out','w')

m,n=map(int,f.readline().split())
n=n%60
m+=n
print(m,file=g)

f.close()
g.close()