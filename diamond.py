n=int(input())
a=n
c=0
r=n-(n//2)+1
for x in range(0,(n//2)+1):
	if(x==0):
		c=1
	else:
		c=c+2
		a=a-2
	for z in range(a//2,0,-1):
		print(" ",end=" ")
	for y in range(0,c):
		print("*",end=" ")
	print()
for i in range(0,r):
	a=a+2
	c=c-2
	for j in range(0,a//2):
		print(" ",end=" ")
	for k in range(0,c):
		print("*",end=" ")
	print()


