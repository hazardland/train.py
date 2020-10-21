import sys
import numpy as np
#from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM
from keras.layers import Dense
import matplotlib.pyplot as plt
import color

plt.style.use('fivethirtyeight')

data = [[[(i+j)/100] for i in range(5)] for j in range(1, 96)]
target = [i/100 for i in range(6, 101)]

data = np.array(data, dtype=float)
print(color.red(data.shape))

target = np.array(target, dtype=float)
print(color.red(target.shape))


print(color.yellow(data.tolist()))
print(color.cyan(target.tolist()))

# x_train, x_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=4)

# print(color.cyan(x_train.tolist()), color.red(y_train.tolist()), color.cyan(x_test.tolist()), color.red(y_test.tolist()))

model = Sequential()
model.add(LSTM(1, batch_input_shape=(None, 5, 1)))
model.add(Dense(4))
model.add(Dense(1))
model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['accuracy'])
model.summary()

print(color.green('Starting training'))
history = model.fit(data, target, epochs=1)
model.save('counter.model')
#print((y_test*100).tolist())
#print(x_test.tolist())
# print(color.cyan(int(model.predict(np.array([[[101./100], [101./100], [103./100], [104./100], [105./100]]], dtype=float))[0][0]*100)))
# print(model.predict(x_test).tolist())
result = model.predict(data)
print(color.yellow(data.tolist()))
print(color.cyan(target.tolist()))
print(color.cyan(result.tolist()))
plt.scatter(range(95), result, c='r')
plt.scatter(range(95), target, c='b')
plt.show()

plt.plot(history.history['loss'])
plt.show()

# right = []
# factual = []

def predict(*args):
    result = model.predict(np.array([[[args[i]/100] for i in range(5)]], dtype=float))
    print(color.yellow([[[args[i]] for i in range(5)]]),
          color.red(args[5]),
          color.cyan(round(result[0][0]*100)))

    # right.append(result[0][0]*100)
    # factual.append(args[5])

predict(1, 2, 3, 4, 5, 6)
predict(13, 14, 15, 16, 17, 18)
predict(30, 31, 32, 33, 34, 35)
# print(len(right))
# print(len(factual))

# plt.scatter(range(100), right, c='r')
# plt.scatter(range(100), factual, c='b')
# plt.show()
