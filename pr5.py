l=[ ]
n=0
while 1:
	item=input("enter the item")
	l.append(item)
	n=input("do you wnat to continue Y/N")
	if n=="n":
		break
	else:
		continue
print("list is ready")
l.sort()
print(l)
	
