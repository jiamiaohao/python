class Person(object):

	instance = None
	#定义__new__方法   不定长参数
	def __new__(cls,*a,**b):
		#如果 cls.instance  是空的
		if cls.instance is None:

			#调用父类__new__方法赋值给cls.instance
			cls.instance = super().__new__(cls)

		return cls.instance
	def __init__(self,name):
 
		self.name = name
		self.skill = "会翻墙"
		print(self.name)
		print(self.skill)

	def __str__(self):
		return

a = Person("潘志伟")
print(id(a))
n = Person("安华凤")
print(id(n))
print(a.name)
print(a)