import urllib.request
import json
z = input('ποιό αρχείο θες   ')

with open(z) as f:
    d = dict(x.rstrip().split(None, 1) for x in f)

a = list(d.keys())
b = [0]*len(a)


def get_coin_data(coin):
    url="https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LTC,XRP,BSV,BCH,EOS,XLM,ADA,YFI&tsyms=EUR&e=CCCAGG"
    r=urllib.request.urlopen(url)
    html=r.read()
    html=html.decode()
    d=json.loads(html)
    return d[coin]["EUR"]
j = 0
for i in d.values() :
    b[j] = get_coin_data(a[j])
    eur = b[j] * int(i)
    print(a[j],eur)
    j += 1
    
