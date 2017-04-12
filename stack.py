class Stack:
	def __init__(self):
		self.data = []
	def push(self,item):
		self.data = self.data + [item]
		#self.data[len(self.data):] =[item]
		#self.data.append(item)
		#print(self.data)
	def pop(self):
		#return self.data.pop()
		tmp = self.data[len(self.data)-1]
		self.data = self.data[:len(self.data)-1]
		return tmp
	
s1 = Stack()
print(s1.data)
#print("please input command:")
#n = raw_input("input command plz:")
#print(n)
flag = 1
while(flag == 1):
	n = raw_input("input command plz:")
	if n == '-1':
		break
	parts = n.split(" ")
	if len(parts) == 1:
		if n[0:3] == 'pop' and len(parts) == 3:
			s1.pop()
		elif n[0:4] == 'push':
			n1 = n[4:len(n)]
			s1.push(n1)
		else:
			 print("input error")
	elif len(parts) == 2:
		if parts[0] == 'push':
			s1.push(parts[1])
		elif parts[0] == 'pop':
			s1.pop()
		else:
			print("input error")
	else:
		print("input error")
	print(s1.data)

