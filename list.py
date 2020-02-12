l=list(map(int,input().split()))
d=[]
for i in l:
	if i not in d:
		d.append(i)
for i in d:
	print(i, end = ' ')
