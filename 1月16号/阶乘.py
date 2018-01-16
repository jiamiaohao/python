#while版阶乘
def calnum(count):
	result = 1
	while count >= 1:
		result*=count
		count -= 1
	return result
chengji = calnum(5)
print(chengji)

#递归函数
def calnum1(num):
	if num > 1:
		return num*calnum1(num-1)
	else:
		return num
print(calnum1(5))

