
for i in range(2,11):
	k = True
	for a in range(2,i):
		if i%a == 0:
			print(a)
			print(i)
			k = False
			break
	if k:
		print(i)

"""

def sushu(a,b):
	list = []
	for i in range(2,b):
		bool = True
		for c in range(2,i):
			if i%c == 0:
				bool = False
				break
		if bool:
			list.append(i)
	print(list)
sushu(1,101)
"""
