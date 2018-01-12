
def sum(a,b,c):
	for i in range(a,b):
		for v in range(a,i+c):
			print("%d×%d=%d"%(v,i,v*i),end="\t")
		print("")
sum(1,10,1)






















