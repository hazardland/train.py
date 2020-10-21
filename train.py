import sys

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import matplotlib.pyplot as plt

import color

scaler = MinMaxScaler()

def diff(n1, n2):
    if n2 is None:
        return color.cyan(' %9f') % n1

    if n1 > n2:
        return color.blue('+%9f') % (n1)
    elif n1 < n2:
        return color.red('-%9f') % (n1)
    else:
        return color.yellow(' %9f') % n1

    # if n2 is None:
    #     return color.black(' %9f') % 0

    # if n1 > n2:
    #     return color.blue('+%9f') % (n1 - n2)
    # elif n1 < n2:
    #     return color.red('-%9f') % (n2 - n1)
    # else:
    #     return color.black(' %9f') % 0

def outcome(n1, n2):
    result = [0, 0, 0]
    if n2 is None:
        return result
    if n1 > n2:
        result[0] = 1
    elif n1 < n2:
        result[1] = 1
    else:
        result[2] = 1
    return result

# print(chart.plot(file1['close'][:130], {'height': 4, 'format':'{:8.0f}'}))
file1 = pd.read_csv('./data/usdt_dash.csv')
file1[['close']] = scaler.fit_transform(file1[['close']])
file1[['volume']] = scaler.fit_transform(file1[['volume']])
file1 = file1.set_index(['date'])

file2 = pd.read_csv('./data/usdt_btc.csv')
file2[['close']] = scaler.fit_transform(file2[['close']])
file2[['volume']] = scaler.fit_transform(file2[['volume']])
file2 = file2.set_index(['date'])

file3 = pd.read_csv('./data/btc_dash.csv')
file3[['close']] = scaler.fit_transform(file3[['close']])
file3[['volume']] = scaler.fit_transform(file3[['volume']])
file3 = file3.set_index(['date'])

history = []
data = []
target = []

file1_close = None
file2_close = None
file3_close = None
file1_volume = None
file2_volume = None
file3_volume = None

i = 0
backtrack = 60
for index, file1_row in file1.iterrows():
    # print(color.cyan(index))
    #print(row)
    try:
        file2_row = file2.loc[index]
        file3_row = file3.loc[index]
        # print(color.yellow('%s found') % index)
    except:
        print(color.red('%s not found') % index)
        continue


    if len(history) >= backtrack:
        data.append(history[i-backtrack:i])
        target.append(outcome(file1_row['close'], file1_close))

    print(
        str(i).rjust(3)+':',
        outcome(file1_row['close'], file1_close),
        diff(file1_row['close'], file1_close),
        diff(file1_row['volume'], file1_volume),
        diff(file2_row['close'], file2_close),
        diff(file2_row['volume'], file2_volume),
        diff(file3_row['close'], file3_close),
        diff(file3_row['volume'], file3_volume)
        # [h[0] for h in data[i-backtrack]] if len(history) >= backtrack else '',
        # target[i-backtrack] if len(history) >= backtrack else ''
        )


    file1_close = file1_row['close']
    file1_volume = file1_row['volume']
    file2_close = file2_row['close']
    file2_volume = file2_row['volume']
    file3_close = file3_row['close']
    file3_volume = file3_row['volume']
    history.append([file1_close, file1_volume, file2_close, file2_volume, file3_close, file3_volume])
    i += 1
    # if i > backtrack+3:
    #     break

# import json
# print(json.dumps(data, indent=4))
'''
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
'''



data = np.array(data, dtype=float)
print(color.red(data.shape))

target = np.array(target, dtype=float)
print(color.red(target.shape))


model = Sequential()
model.add(LSTM(50, return_sequences=True, batch_input_shape=(None, backtrack, 6)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25)) #, activation='relu')
model.add(Dense(3)) #, activation='relu')
model.compile(loss='mean_squared_error', optimizer='adam', metrics=['accuracy'])
model.summary()


print(color.green('Starting training'))
history = model.fit(data, target, epochs=20)

model.save('train.model')

plt.plot(history.history['loss'])
plt.show()

sys.exit()

#print((y_test*100).tolist())
#print(x_test.tolist())
# print(color.cyan(int(model.predict(np.array([[[101./100], [101./100], [103./100], [104./100], [105./100]]], dtype=float))[0][0]*100)))
# print(model.predict(x_test).tolist())
result = model.predict(data)
print(color.yellow(data.tolist()))
print(color.cyan(target.tolist()))
print(color.cyan(result.tolist()))

plt.style.use('fivethirtyeight')

plt.scatter(range(95), result, c='r')
plt.scatter(range(95), target, c='b')
plt.show()

plt.plot(history.history['loss'])
plt.show()
