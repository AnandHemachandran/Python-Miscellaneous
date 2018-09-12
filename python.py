n=int(input())
c=0
a=n
for x in range(0,n):
	c=c+1
	for  y in range(0,c):
		print("*", end=" ")
	print()
	
for x in range(0,n):
	a=a-1
	for  y in range(0,a):
		print("*", end=" ")
	print()
	
	
