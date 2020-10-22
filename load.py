import keras
from prepare import prepare
import numpy as np
import color

data, target = prepare('./data/usdt_dash.csv', './data/usdt_btc.csv', './data/btc_dash.csv')

model = keras.models.load_model('./train.model')

i = 0
for item in data:
    pred = model.predict(np.array([data[i]], dtype=float))[0]
    pred_text = ''
    if pred[0] > pred[1] and pred[0] > pred[2]:
        pred_text = 'up'
    elif pred[1] > pred[0] and pred[1] > pred[2]:
        pred_text = 'down'
    else:
        pred_text = 'steady'
    target_text = ''
    if target[0] > target[1] and target[0] > target[2]:
        target_text = 'up'
    elif target[1] > target[0] and target[1] > target[2]:
        target_text = 'down'
    else:
        target_text = 'steady'
    if target_text==pred_text:
        print(color.red(target[i]), color.red(pred))
    else:
        print(target[i], pred)
    i += 1
