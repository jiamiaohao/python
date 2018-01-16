
"""

def print_sum(a=100):
	sum = 0
	for i in range(1,a+1):
		sum+=i
	return sum

relust =print_sum()
print(result)




"""
"""
def sum(a,b,*c,**d):
	g = a+b
	print(a)
	print(b)
	print(c)
	print(d)
	return g

result = sum(66,44,8,4,3,2,name=3,age=0)
print(result)


"""



def sum(a,b,c,*d,**e):

	sum1 = 0
	sum2 = 0
	sum3 = a+b+c
	for i in d:
		sum1+=i
	for k,v in e.items():
		sum2+=v
	o = sum3 + sum1 + sum2
	return o
		
t = sum(1,2,3,4,5,6,7,name=8,age=9)
print(t)





def m(a,b,c,*d,**e):
	sum = a+b+c
	sum1 = 0
	sum2 = 0
	for i in d:
		sum1+=i
	for k,v in e.items():
		sum2+=v
	p = sum + sum1 + sum2
	return p

l = m(43,23,42,66,77,8,9,name=2,age=7)
print(l)







