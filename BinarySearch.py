#def


a = []
while(1):
	b = input("input a number(finish with -1):")
	if b == -1:
		break
	if a == []:
		a.append(b)
	else:
		if b < a[len(a)-1]:
			a.append(a[len(a)-1])
			i = len(a)-2
			while(i > -1):
				if b < a[i]:
					a[i+1] = a[i]
				else:
					a[i+1] = b
					break
				i = i-1
			if i == -1:
				a[i+1] = b
		else:
			a.append(b)
print(a)
