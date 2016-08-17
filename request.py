import requests
url = 'http://www.littlebigplay.com/submitAir.php'
payload = {'nickname': 'NULL', 'gameid': 
'145','gameMode':'3','score':'2147483647'}
while True:
	r = requests.post(url,data=payload)
	print (r.text,r.status_code)
