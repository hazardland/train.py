import keras
import matplotlib.pyplot as plt
import numpy as np
from prepare import prepare
import color

data, target = prepare('./data/usdt_dash_2.csv', './data/usdt_btc_2.csv', './data/btc_dash_2.csv')

model = keras.models.load_model('./train.model')



pred = model.predict(np.array(data, dtype=float))

i = 0
for item in data:
    print(target[i], pred[i])
    i += 1


plt.plot(target, color='blue')
plt.plot(pred, color='red')
plt.show()
