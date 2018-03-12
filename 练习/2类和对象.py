# class Person(object):

# 	def __init__(self,name,age,height):
# 		self.name = name
# 		self.age = age
# 		self.height = height

# 	def run(self):
# 		print("%s今年%d岁,身高%.2f,每天早上跑完步,会去吃东西"%(self.name,self.age,self.height))

# 	def eat(self):
# 		print("%s今年%d岁,身高%.2f,%s不跑步,%s喜欢吃东西"%(self.name,self.age,self.height,self.name,self.name))


# xiaoming = Person("小明",15,1.65)
# xiaoming.run()
# xiaomei = Person("小美",17,1.56)
# xiaomei.eat()






# class Animal(object):

# 	def __init__(self,name,phone):
# 		self.name = name
# 		self.phone = phone

# 	def eat(self):
# 		print("%s他没在家，他的电话是%d"%(self.name,self.phone))

# 	def run(self):
# 		print("%s他出差了，他的手机号是%d"%(self.name,self.phone))

# s = Animal("小红",11111111111)
# s.eat()
# s = Animal("小黑",66666666666)
# s.run()




class Tool(object):

	def __init__(self,name,materials,function):
		self.name = name
		self.materials = materials
		self.function = function

	def axu(self):
		print("您选的工具为：%s"%self.name)
		print("您选的工具材质为:%s"%self.materials)
		print("他的功能为:%s"%self.function)


class Weapon(Tool):

	def __init__(self,wpn_name,wpn_materials,wpn_function):
		self.wpn_name = wpn_name
		self.wpn_materials = wpn_materials
		self.wpn_function = wpn_function

	def chain(self):
		print("武器名为:%s"%self.wpn_name)
		print("材质为:%s"%self.wpn_materials)
		print("功能：%s"%self.wpn_function)

# a = Tool("斧头","铁、木头","劈、砍")
# a.axu()
b = Weapon("链子","铁","缠绕")
b.chain()
b.axu()




