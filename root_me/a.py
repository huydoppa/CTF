data = "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47"

def f1(x,y):
	return x^y

def f2(y):
	z = 0
	for i in range (0,y):
		z += pow(2,i)
	return z

def f3(y):
	z = 0
	for i in range(8-y,8):
		z += pow(2,i)
	return z

def f4(x,y):
	y = y%8
	I = f2(y)
	I = (x&I) << (8-y)
	return (I) +(x>>y)

def f5(x,y):
	y = y % 8
	I = f3(y)
	I = (x&I) >> (8-y)
	return (I) + (x>>y)
def f6(x,y):
	return f5(x,y)
def f7(v9,key):
	v8 = ""
	v82 = ""
	for i in range(0,len(v9)):
		c = ord(v9[i])
		if (i!=0):
			t = ord(v8[i-1])%2
			if(t==0):
				cr = f1(c,ord(key[i%len(key)]))
				break
			if(t==1):
				cr = f6(c,ord(key[i%len(key)]))
				break
		else :
			cr = f1(c,ord(key[i%len(key)]))
		v8 += str(cr)
		print(cr)
#	return v8
f7(data,"flag")

