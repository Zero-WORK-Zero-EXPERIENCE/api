import requests

stuff = requests.get("https://gtaupdate.com/gta/")

print(stuff.text)

# /html/body/center[2]/table/tbody/tr[2]/td[1]