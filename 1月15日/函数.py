
def sum1(a,b):
	j = 0
	o = 0
	sum = 0
	for i in range(a,b):
		if i%2 == 0:
			o+=i
		if i%2 != 0:
			j+=i
	sum = j+o
	print("奇数：%d 偶数:%d 和:%d"%(j,o,sum))
sum1(1,101)
