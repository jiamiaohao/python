class Person(object):
	def play_computergames(self):
		print("玩游戏")

	def sleep(self):
		print("该睡觉了")

class Father(Person):
	def __init__(self,name):
		self.name = name

	def play_computergames(self):
		print("%s在玩游戏"%self.name) 

class Mather(Person):
	def __init__(self,name):
		self.name = name

	def sleep(self):
		print("%s累了，要睡觉"%self.name)


class Son(object):
	instance = None
	is_instance = False

	def __new__(cls,*q,**w):
		if Son.instance is None:
			cls.instance = super().__new__(cls)
		return cls.instance
	def __init__(self,name):
		
		if not Son.is_instance:
			print("我是爸爸妈妈唯一的孩子")
			self.name = name
			Son.is_instance = True

	def play_with_family(self,Father,Mather):
		print("%s和%s%s出去旅游了"%(self.name,Father.name,Mather.name))


baba = Father("爸爸")
baba.play_computergames()

mama = Mather("妈妈")
mama.sleep()

xiaoming = Son("小明")
xiaoming.play_with_family(baba,mama)
