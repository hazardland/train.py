import json
import poloniex.public
from pandas.io.json import json_normalize

result = poloniex.public.returnChartData('USDT_DASH', '2019-11-09 20:00:00', '2019-11-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/usdt_dash.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('USDT_BTC', '2019-11-09 20:00:00', '2019-11-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/usdt_btc.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('BTC_DASH', '2019-11-09 20:00:00', '2019-11-12 20:30:00', 300)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/btc_dash.csv', index=False, encoding='utf-8')