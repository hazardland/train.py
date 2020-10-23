import sys

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

import matplotlib.pyplot as plt

from prep2 import prepare
import color

data, target = prepare('./data/XRP_usdt_xrp_train.csv',
                       './data/XRP_usdt_btc_train.csv',
                       './data/XRP_btc_xrp_train.csv')


data = np.array(data, dtype=float)
print(color.red(data.shape))

target = np.array(target, dtype=float)
print(color.red(target.shape))

model = Sequential([
    Dense(units=6*30*2, input_shape=(6*30,)),
    Dense(units=32),
    Dense(units=1)
])

model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='mse',
              metrics=['accuracy'])

history = model.fit(x=data,
                    y=target,
                    batch_size=10,
                    epochs=100,
                    shuffle=True,
                    verbose=2,
                    validation_split=0.1)

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
