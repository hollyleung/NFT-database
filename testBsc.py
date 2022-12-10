from math import fabs
import requests
import time
import pandas as pd

now = int(time.time())
#one_hour_ago = now - 3600

# addr = "STEPNq2UGeGSzCyGVr2nMQAzf8xuejwqebd84wcksCK"

headers = {'Content-type': "application/x-www-form-urlencoded"}

url = "https://api.bscscan.com/api?module=account&action=tokentx&contractaddress=0x3944aC66b9b9B40a6474022D6962b6cAA001b5E3&address=0x0000000000000000000000000000000000000000&startblock=0&endblock=99999999&page=1&offset=10000&sort=desc&apikey=TN7K949JF17KFRQCMG5UVXPUGBHPJ5WBXV"

r = requests.get(url, headers=headers)

res = r.json()

df = pd.DataFrame.from_dict(res.get('result'))


# res = res.split("\n")
# res = [lines.strip().split(',') for lines in res]

# print(res[0])
# print(res[1])
# print(res[2])

# df = pd.DataFrame(res[1:], columns =res[0])
# print(df)
df.to_csv('Elpis.csv', index=False)
print(df)

# df = pd.read_csv(r.content.decode(), sep="\n")

# print(df)


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
# }

# params = {
#     'account': 'EArf8AxBi44QxFVnSab9gZpXTxVGiAX2YCLokccr1UsW',
#     'type': 'tokenchange',
#     'fromTime': one_hour_ago,
#     'toTime': now
# }

# response = requests.get('https://api.solscan.io/account/exportTransactions', headers=headers, params=params)

# print(response.content.decode())