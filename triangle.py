def checktriangle(a,b,c):
	if(a+b>c):
		if(a+c>b):
			if(b+c>a):
				print("Triangle is valid")

def setupedges():
	edge=[]
	for i in range(0,3):
		edge.append(int(input()))

	return edge
def main():
	side=setupedges()
	checktriangle(side[0],side[1],side[2])
	return
main()
