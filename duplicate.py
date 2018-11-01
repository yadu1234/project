list1=[]
print("Enter the range:")
k=int(input())
print("Enter the data:")
for i in range(0,k):
	list1.append(int(input()))
list2=list1
for j in list2:
	if(list2[j]==list2[j+1]):
		continue
	else:
		count=0
		for i in list1:
			print(list2[j])
			if(list2[j]==list1[i]):
				count=count+1
	if(count%2==0):
		pair=(count/2)
		print("No: of pairs:",pair)
	else:
		pair=int(count/2)
		print("No: of pairs:",pair)
