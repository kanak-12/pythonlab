print(" enter element in 1 string")
l1=list(map(int,input().split()))
print("enter element in 2 string")
l2=list(map(int,input().split()))
l=[i for i in l1 if i in l2]
print("common elements")
print(l)
