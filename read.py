import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

ax = plt.gca()
scaler = MinMaxScaler()

usdt_dash = pd.read_csv('./data/usdt_dash.csv')
usdt_dash[['close']] = scaler.fit_transform(usdt_dash[['close']])
usdt_dash[['volume']] = scaler.fit_transform(usdt_dash[['volume']])
# usdt_dash.plot(kind='line', x='date', y='usdt dash volume', color='red', ax=ax)
usdt_dash.plot(kind='line', x='date', y='close', color='blue', ax=ax)


usdt_btc = pd.read_csv('./data/usdt_btc.csv')
usdt_btc[['close']] = scaler.fit_transform(usdt_btc[['close']])
usdt_btc[['volume']] = scaler.fit_transform(usdt_btc[['volume']])
# usdt_btc.plot(kind='line', x='date', y='btc dash volume', color='green', ax=ax)
usdt_btc.plot(kind='line', x='date', y='close', color='red', ax=ax)


btc_dash = pd.read_csv('./data/btc_dash.csv')
btc_dash[['close']] = scaler.fit_transform(btc_dash[['close']])
btc_dash[['volume']] = scaler.fit_transform(btc_dash[['volume']])
# btc_dash.plot(kind='line', x='date', y='btc dash volume', color='green', ax=ax)
btc_dash.plot(kind='line', x='date', y='close', color='yellow', ax=ax)

plt.show()
