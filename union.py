l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
d=[i for i in l2 if i not in l1]
l1.extend(d)

print(l1)
