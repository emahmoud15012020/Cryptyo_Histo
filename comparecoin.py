import pandas as pd
import requests
from crycompare import price as p
from crycompare import history as h


API_KEY = '051999c8-7279-46f2-9261-0b8c480d25ec'

headers = {
    'X-CMC_PRO_API_KEY': API_KEY
}

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
r = requests.get(url,headers=headers)
df_dict = {}
if r.status_code == 200:
    data = r.json()
    for d in data['data'][:100]:
        coin = d['symbol']
        histo = h.histo_day(coin, 'USD',all_data=True,limit=1000)
        try :
                df_histo = pd.DataFrame(histo)
                df_histo['time'] = pd.to_datetime(df_histo['time'], unit='s')
                df_histo.index = df_histo['time']
                del df_histo['time']
                del df_histo['volumefrom']
                del df_histo['volumeto']
                df_dict[coin] = df_histo
        except:
            pass
    crypto_histo = pd.concat(df_dict.values(), axis=1, keys=df_dict.keys())
    print("END")

