import keras
import matplotlib.pyplot as plt
import numpy as np
from prepare import prepare
import color

data, target = prepare('./data/usdt_xrp_1.csv',
                       './data/usdt_btc_1.csv',
                       './data/btc_xrp_1.csv')

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
            print('real',color.cyan(target[i]), real_text, '| predict', color.cyan(pred[i]),  pred_text)
        else:
            print('real', target[i], real_text, '| predict', pred[i],  pred_text)

    i += 1


plt.plot(target, color='blue')
plt.plot(pred, color='red')
plt.show()
