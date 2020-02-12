n=list(map(int,input().split()))
d=[]
for i in n:
	if i not in d:
		d.append(i)
print(*d,sep='*')
