

def runnian(a):

	if (a%400 == 0) or (a%4 == 0 and a%100 != 0):
		print("闰年")
	else:
		print("平年")
runnian(2000)

