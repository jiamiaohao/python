
# 0:表示文件的开头
# 1:表示当前位置
# 2:表示文件末尾
#要想让文件一末尾为起始倒着读写的话必须在打开文件时候让文件以f = open("text.txt","rb+"")的方式打开


f = open("text.txt","rb+")
str = f.read(3)
print("读取的数据是：",str)

#查找当前位置
position = f.tell()
print("当前文件位置为：",position)


#重新设置位置
f.seek(5,0)

#查找当前位置
position = f.tell()
print("当前文件位置为：",position)

#重新设置位置离文件末尾处3个字节处
f.seek(-3,2)

#读取到的数据为：文件最后3个字节数据
str = f.read()
print("读取的数据是：",str)

f.close()


