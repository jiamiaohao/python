
tip = "酒窖仓库储存管理系统"
print(tip.center(50,"*"))
list = []
#登录模块
def denglu():
	count = 3
	a = True
	while a:
		password = '000000'
		passwd = input("请输入密码：")
		if password == passwd:
			print("登陆成功")
			gongneng()
			a = False
		else:
			print("密码错误，还有",count-1,"次机会！")
		if count==1:
			print("错误次数过多，账号被锁！")
			a = False
		count-=1

#入库模块
def pinming():
	dict = {}
	jiuming = input("请输入要入库酒的品名：")
	shuliang = input("请输入入库数量：")
	if not list:
		dict["name"] = jiuming
		dict["count"] = shuliang
		list.append(dict)
		print("入库成功！")
	else:
		isrepeat = False
		for i in list:
			for k,v in i.items():
				if v == jiuming:
					print("你输入重复了，可以直接修改功能！")
					isrepeat = True
					break
		if not isrepeat:
			dict["name"] = jiuming
			dict["count"] = shuliang
			list.append(dict)
			
#修改模块
def xiugai():
	xiugai = False
	xiujiuming = input("请输入要修改的名字：")
	change_name = input("名字修改为：")
	change_num = input("数量修改为：")
	for i in list:
		if i['name'] == xiujiuming:
			i['name'] = change_name
			i['count'] = change_num	
			xiugai = True
			break
	if xiugai == False:
		print("系统中没有你要修改的信息")
#删除模块
def shanchu():
	shanchu = False
	shanjiuming = input("请输入要删除的名字：")
	for i in list:
		for k,v in i.items():
			if v == shanjiuming:
				list.remove(i)
				shanchu = True
				break
	if shanchu == False:
		print("系统中没有你要删除的信息")
	print(list)

#查看模块
def chakan():
	find = False
	chajiuming = input("请输入要查看的酒名：")
	for i in list:
		if i['name'] == chajiuming:
			print(i)
			find = True
			break
			
	if find == False:
		print("当前系统中未储存此酒")



def gongneng():
	while True:
		gongneng = int(input("请选择功能：1、添加品名或数量  2、修改品名或数量  3、删除  4、查看数量  5、退出酒窖仓库管理系统  "))
		print("*"*60)
		if gongneng == 1:
			pinming()
		elif gongneng == 2:
			xiugai()
		elif gongneng == 3:
			shanchu()
		elif gongneng == 4:	
			chakan()
		elif gongneng == 5:
			print("欢迎再次使用")
			break
denglu()
