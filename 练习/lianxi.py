#植物类
class Botany(object):


	#定义方法  晃动
	def waggle(self):
		print("晃动产生阳光")

	#定义方法  眩晕
	def dizziness(self):
		print("眩晕、迷惑")	

	#定义方法  射子弹
	def bullet(self):
		print("射子弹:吐 、吐 、 吐")

	#定义方法  冰冻
	def frozen(self):
		print("冰冻减速：慢 、 慢 、 慢")

	#定义方法  连射
	def dartle(self):
		print("四连射：突突突突 、 突突突突 、 突突突突")

#辅助类
class Assist(Botany):
	#初始化  名字、血量
	def __init__(self,name,blood):
		self.name = name
		self.blood = blood
		print(self.name)
		print(self.blood)


#攻击类
class Attack(Botany):
	#初始化  名字、血量
	def __init__(self,name,blood):
		self.name = name
		self.blood = blood
		print(self.name)
		print(self.blood)


#实例太阳花
sunflower = Assist("太阳花","3格血")
sunflower.waggle()

print("*"*25)

#实例豌豆射手
peashooter = Attack("豌豆射手","7格血")
peashooter.bullet()

print("*"*25)

#实例寒冰射手
ashe = Attack("寒冰射手","6格血")
ashe.bullet()
ashe.frozen()

print("*"*25)

#实例寒冰机枪射手
stutterer = Attack("机枪射手","8格血")
stutterer.dartle()
stutterer.frozen()

#僵尸类
class Zombie(object):
	pass