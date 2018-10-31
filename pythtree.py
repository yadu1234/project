l=[]
b=[]
print("Enter the no:s")
l=input()
a=l.split(" ")
for i in a:
	b.append(int(i))
for i in range(0,len(l)):
	#print(l[i])
	for j in range(0,i+1):
		print(b[j],end=" ")
	print("\r")
