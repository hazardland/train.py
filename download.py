import json
import poloniex.public
from pandas.io.json import json_normalize

currency = 'XRP'

date_train_from = '2020-08-01 00:00:00'
date_train_to = '2020-08-30 23:59:59'

date_test_from = '2020-10-01 00:00:00'
date_test_to = '2020-10-30 23:59:59'

scope = 300

result = poloniex.public.returnChartData('USDT_'+currency, date_train_from, date_train_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_usdt_xrp_train.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('USDT_BTC', date_train_from, date_train_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_usdt_btc_train.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('BTC_'+currency, date_train_from, date_train_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_btc_xrp_train.csv', index=False, encoding='utf-8')


result = poloniex.public.returnChartData('USDT_'+currency, date_test_from, date_test_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_usdt_xrp_test.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('USDT_BTC', date_test_from, date_test_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_usdt_btc_test.csv', index=False, encoding='utf-8')

result = poloniex.public.returnChartData('BTC_'+currency, date_test_from, date_test_to, scope)
data = json_normalize(json.loads(result.read()))
data.to_csv('data/'+currency+'_btc_xrp_test.csv', index=False, encoding='utf-8')
