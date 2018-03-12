#定义家具类
class Houseltem:
	#初始化  名字   占地面积
	def __init__(self,name,area):

		self.name = name
		self.area = area

	def __str__(self):
		#格式话输出  名字   占地面积
		a = "[%s],占地面积为:%.2f"%(self.name,self.area)
		return a


#实例化  席梦思
bed = Houseltem("席梦思",4)
print(bed)
print("*"*20)
chest = Houseltem("衣柜",2)
print(chest)
print("*"*20)
table = Houseltem("餐桌",1.5)
print(table)


#定义房子类
class House:
	#初始化    户型   总面积
	def __init__(self,house_type,total_area,):

		self.house_type = house_type
		self.total_area = total_area
		#剩余面积 = 总面积  (因为还没有添加家具，列表还为空)
		self.sheng_area = total_area
		#定义一个空列表
		self.item_list = []

	def __str__(self):

		b = "户型为：%s,总面积为：%.2f,[剩余面积为：%.2f],添加的家具：%s"%(self.house_type,self.total_area,self.sheng_area,self.item_list)
		return b

	def add_item(self,Item):
		#判断 家具面积  是否大于  剩余面积
		if Item.area > self.sheng_area:
			print("%s面积太大了，装不下了"%Item.name)
			return
		#往列表添加家具名字
		self.item_list.append(Item.name)
		self.sheng_area -= Item.area

san = House("一室一厅",85)
san.add_item(bed)
san.add_item(chest)
san.add_item(table)
print(san)







