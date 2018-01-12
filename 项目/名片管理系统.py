
tip = "学生人员信息管理系统"
print(tip.center(50,"*"))

list = []
while True:
	mode = int(input("请选择功能 1、新增  2、查看  3、修改  4、删除  5、退出："))
#新增功能
	if mode == 1:
		dic = {}
		youname = input("输入名姓名：")
		youage = int(input("输入年龄："))
		yousex = input("输入性别：")
		youculture = input("输入学历：")
		if not list:
			dic["name"] = youname
			dic["age"] = youage
			dic["sex"] = yousex
			dic["culture"] = youculture
			list.append(dic)
			print(list)
		else:
			isrepeat = False
			for i in list:
				for k,v in i.items():
					if v == youname:
						print("你输入重复了")
						isrepeat = True
						break
			if not isrepeat:
				dic["name"] = youname
				dic["age"] = youage
				dic["sex"] = yousex
				dic["culture"] = youculture
				list.append(dic)		
		for i in list:
			print(i)

#查看功能
	if mode == 2:
		  
		name1 = input("输入查询人的姓名：")
		for i in list:
			for k,v in i.items():
				if v == name1:
					print(i)
					break
				else:
					print("没有你要查寻的人")
					break
#修改功能
	if mode == 3:
		change_name = input("请输入你要修改的用户：")
		change_age = int(input("输入修改的年龄："))		
		change_sex = input("输入修改的性别：")		
		change_culture = input("输入修改的学历：")		
		for i in list:
			if i['name'] == change_name:
				i['age'] = change_age
				i['sex'] = change_sex
				i['culture'] = change_culture
				break

#删除功能s
	if mode == 4:
		del_name = input("请输入要删除人的姓名：")
		del_age = input("请输入要删除人的年龄：")
		del_sex = input("请输入要删除人的性别：")
		del_culture = input("请输入要删除人的学历：")
		for i in list:
			if i['name'] == del_name:
				i['age'] = del_age
				i['sex'] = del_sex
				i['culture'] = del_culture
				list.remove(i)
				
#退出功能
	if mode == 5:
		break















