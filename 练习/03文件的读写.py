a = open("text.txt","r")
b = a.read()
print(b)
print("*"*15)
a = open("text.txt","r")
c = a.read(5)
print(c)
a.close()


f = open("text.txt","r")
content = f.readlines()
print(type(content))
i = 1
for temp in content:
	print("%d:%s"%(i,temp))
	i += 1

f.close()