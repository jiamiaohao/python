class A(object):
	def __init__(self,name):
		self.name = name
		self.list = [3,5,84,"nihao","haha"]



	def shuo(self):
		print("%s,小红"%self.name)
		for i in self.list:
			a = "nihao" + str(i)
			print(a)


class B(A):
	def bshuo(self):
		print("wo 是b")




b = B("你好")
b.shuo()
b.bshuo()
