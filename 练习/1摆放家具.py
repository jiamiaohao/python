class Houseltem:

	def __init__(self,name,zhan_area):
		
		self.name = name
		self.zhan_area = zhan_area

	def zhan(self):

		print("%s，占地：%.2f平方米"%(self.name,self.zhan_area))

bed = Houseltem("席梦思",4)
bed.zhan()
chest = Houseltem("衣柜",2)
chest.zhan()
table = Houseltem("餐桌",1.5)
table.zhan()



class