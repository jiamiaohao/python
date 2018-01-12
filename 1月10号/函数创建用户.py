def a():
	list = []
	while True:
		dic = {}
		name = input("请输入名字：")
		age = input("请输入年龄：")
		if not list:
			dic["name"] = name
			dic["age"] = age
			list.append(dic)
		else:
			isrepeat = False
			for i in list:
				for k,v in i.items():
					if v == name:
						print("你输入重复了")
						isrepeat = True
						break
			if not isrepeat:
				dic["name"] = name
				dic["age"] = age
				list.append(dic)
		for i in list:
			print(i)
a()	
