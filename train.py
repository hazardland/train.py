import sys

import numpy as np
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
from keras.layers import Dropout
import matplotlib.pyplot as plt

from prepare import prepare
import color

data, target = prepare('./data/usdt_dash.csv', './data/usdt_btc.csv', './data/btc_dash.csv')


data = np.array(data, dtype=float)
print(color.red(data.shape))

target = np.array(target, dtype=float)
print(color.red(target.shape))


model = Sequential()

model.add(LSTM(60, return_sequences=True, batch_input_shape=(None, 60, 6)))
model.add(Dropout(0.35))

model.add(LSTM(100, return_sequences=False))
model.add(Dropout(0.35))

model.add(Dense(3))
# mean_squared_error, mean_squared_error
model.compile(loss='mse', optimizer='rmsprop', metrics=['accuracy'])
model.summary()


print(color.green('Starting training'))
history = model.fit(data, target, epochs=100)

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
