#吃鸡


def chuangjian():
	pit_account = input("请输入创建的账号：")
	pit_passwd = input("请输入创建的密码：")
	print("创建成功")
	denglu(pit_account,pit_passwd)

def denglu(pit_account,pit_passwd):
	account = input("请输入登录账号：")
	passwd = input("请输入登录密码：")
	if account == pit_account and passwd == pit_passwd:
		print("登录成功")







	else:
		print("登录失败")


def jianzhuangbei():







chuangjian()
	









