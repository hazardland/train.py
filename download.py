import json
import poloniex.public
from pandas.io.json import json_normalize

result = poloniex.public.returnChartData('USDT_XRP', '2020-08-09 20:00:00', '2020-08-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/usdt_xrp_2.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('USDT_BTC', '2020-08-09 20:00:00', '2020-08-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/usdt_btc_2.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('BTC_XRP', '2020-08-09 20:00:00', '2020-08-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/btc_xrp_2.csv', index=False, encoding='utf-8')
