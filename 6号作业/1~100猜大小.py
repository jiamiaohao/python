import random
x = random.randint(1,100)
for a in range(0,10):
	b = int(input("请随机输入1-100："))
	if x > b:
		print("不好意思，你猜小了")
	if x < b:
		print("不好意思，你猜大了")
	if x == b:
		print("恭喜你，猜对了")
		break













