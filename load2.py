import keras
import matplotlib.pyplot as plt
import numpy as np
from prep2 import prepare
import color
import sys

data, target = prepare('./data/XRP_usdt_xrp_test.csv',
                       './data/XRP_usdt_btc_test.csv',
                       './data/XRP_btc_xrp_test.csv')

model = keras.models.load_model('./train.model')

pred = model.predict(np.array(data, dtype=float))

i = 0
for item in data:
    if i > 0:
        real_text = 'steady'
        if target[i] > target[i-1]:
            real_text = 'up'
        elif target[i] < target[i-1]:
            real_text = 'down'

        pred_text = 'steady'
        if pred[i] > target[i-1]:
            pred_text = 'up'
        elif pred[i] < target[i-1]:
            pred_text = 'down'

        if real_text == pred_text:
            print('real', color.cyan(target[i]), real_text, '| predict', color.cyan(pred[i]), pred_text)
        else:
            print('real', target[i], real_text, '| predict', pred[i], pred_text)

    i += 1


plt.plot(target, color='blue')
plt.plot(pred, color='red')
plt.show()
