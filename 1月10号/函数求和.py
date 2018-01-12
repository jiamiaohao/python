def print_sum():
	sum1 = 0
	sum2 = 0
	for i in range(1,101):
		if i%2 == 0:
			sum1 += i
		elif i%2 != 0:
			sum2 += i
	sum = sum1 + sum2						

	print("偶数%d"%sum1)
	print("奇数%d"%sum2)
	print("总和%d"%sum)
print_sum()



