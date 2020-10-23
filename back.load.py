import keras
import matplotlib.pyplot as plt
import numpy as np
from prepare import prepare
import color
import sys

data, target = prepare('./data/XRP_usdt_xrp_2.csv',
                       './data/XRP_usdt_btc_2.csv',
                       './data/XRP_btc_xrp_2.csv')

model = keras.models.load_model('./train.model')



pred = model.predict(np.array(data[0], dtype=float))

print(pred[0])
sys.exit()

i = 0
for item in data:
    if i > 0:
        real_text = 'steady'
        if target[i][0] > target[i-1][0]:
            real_text = 'up'
        elif target[i][0] < target[i-1][0]:
            real_text = 'down'

        pred_text = 'steady'
        if pred[i][0] > target[i-1][0]:
            pred_text = 'up'
        elif pred[i][0] < target[i-1][0]:
            pred_text = 'down'

        if real_text == pred_text:
            print('real', color.cyan(target[i]), real_text, '| predict', color.cyan(pred[i]), pred_text)
        else:
            print('real', target[i], real_text, '| predict', pred[i], pred_text)

    i += 1


plt.plot(target, color='blue')
plt.plot(pred, color='red')
plt.show()
