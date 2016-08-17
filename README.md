# Request
### Nedir ?
HTML form gönderme işlemini python2.x kullanarak gönderme işlemidir.
### Neden ?
Canımız sıkıldı yaptık
### Nasıl ?
- [Requests](https://github.com/kennethreitz/requests/) librarysi import edilir.
```py
import requests
```
- POST edilecek url girilir
```py
url = 'http://www.littlebigplay.com/submitAir.php'
```
- Veriler payload alanına özellik ve değerleri şeklinde girilir. Örn: {'name':'value'}
```py
payload = {'nickname': 'NULL', 'gameid':'145','gameMode':'3','score':'2147483647'}
```
- Cevabımız gönderilir
```py
r = requests.post(url,data=payload)
```

**Bu script Rabbit the Climber oyununun skor gönderme açığından yararlanılarak yazılmıştır. Not: özür dileriz :( **
