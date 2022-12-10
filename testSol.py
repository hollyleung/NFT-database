from math import fabs
import requests
import time
import pandas as pd

now = int(time.time())
one_hour_ago = now - 3600

addr = "STEPNq2UGeGSzCyGVr2nMQAzf8xuejwqebd84wcksCK"

url = "https://public-api.solscan.io/account/exportTransactions?account={0}&type=tokenchange&fromTime={1}&toTime={2}".format(addr, one_hour_ago, now)

r = requests.get(url)

res = r.text

res = res.split("\n")
res = [lines.strip().split(',') for lines in res]

# print(res[0])
# print(res[1])
# print(res[2])

df = pd.DataFrame(res[1:], columns =res[0])
# print(df)
df.to_csv('out.csv', index=False)

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