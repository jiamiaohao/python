class Fly_ji(object):
	
	def red(self):
		print("红色")

	def yellow(self):
		print("黄色")

class Fly_ji_one(Fly_ji):
	
	def __init__(self,name):
		name = input("请输入名字：")
		self.name = name
		print("%s战机"%self.name)


class Fly_ji_tow(Fly_ji_one):
	
	instance = None
	j = False
	def __new__(cls,*n,**m):
		
		if Fly_ji_tow.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance

	def __init__(self,name):


		if not Fly_ji_tow.j:
			name = input("请输入名字：")
			self.name = name
			print("我是唯一一个特例的飞机")

			Fly_ji_tow.j = True


b = Fly_ji_one("")
b.yellow()

a = Fly_ji_tow("")
a.red()