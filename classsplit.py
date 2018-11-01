class Try:
	def __init__(self, value):
		self.value=value
	def print(self):
		tem=self.value.split(" ")
		print(tem)
print("Enter the values:")
c=input()
t=Try(c)
print("List:")
t.print()
