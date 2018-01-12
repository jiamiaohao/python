

def shuru():
	year = int(input("请输入年份："))
	month = int(input("请输入月份："))
	day = int(input("请输入日期："))



	count_day(year,month,day)


def count_day(year,month,day1):
	day=0
	da_month = [1,3,5,7,8,10,12]
	xiao_month = [4,6,9,11]
	for i in range(1,month):
		if i in da_month:
			day+=31
		elif i in xiao_month:
			day+=30
		else:
			if runnian(year) == True:
				day+=29
			else:
				day+=28
	day+=day1
	print("%d"%day)

def runnian(year):
	if (year%4 == 0 and year%100 != 0) or year%400 == 0:
		return 1
	else:
		return 0

shuru()
































