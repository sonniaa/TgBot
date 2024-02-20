import requests
with open('bott.txt') as f:
    token = f.read()

endPoint = f'https://api.telegram.org/bot{token}/getMe'
res = requests.get(endPoint)
print(res.status_code)