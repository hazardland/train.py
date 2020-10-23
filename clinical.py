from random import randint
from sklearn.preprocessing import MinMaxScaler
from sklearn.utils import shuffle
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


train_samples = []
train_labels = []

for i in range(50):
    # 5% of younger inividuals who suffered from side effects
    train_samples.append(randint(13, 64))
    train_labels.append(1)

    # 5% of older inividuals who did not experience side effects
    train_samples.append(randint(64, 100))
    train_labels.append(0)

for i in range(1000):
    # 95% of younger inividuals who did not experience side effects
    train_samples.append(randint(13, 64))
    train_labels.append(0)

    # 95% of older inividuals who suffered from side effects
    train_samples.append(randint(64, 100))
    train_labels.append(1)

train_samples = np.array(train_samples)
train_labels = np.array(train_labels)

train_samples, train_labels = shuffle(train_samples, train_labels)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_train_samples = scaler.fit_transform(train_samples.reshape(-1, 1))

# print(scaled_train_samples.tolist())
# print(train_labels.tolist())

model = Sequential([
    Dense(units=16, input_shape=(1,), activation='relu'),
    Dense(units=32, activation='relu'),
    Dense(units=2, activation='softmax')
])

model.summary()

model.compile(optimizer=Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x=scaled_train_samples,
          y=train_labels,
          batch_size=10,
          epochs=100,
          shuffle=True,
          verbose=2,
          validation_split=0.1)

test_samples = []
test_labels = []

for i in range(20):
    # 5% of younger inividuals who suffered from side effects
    test_samples.append(randint(13, 64))
    test_labels.append(1)

    # 5% of older inividuals who did not experience side effects
    test_samples.append(randint(64, 100))
    test_labels.append(0)

for i in range(200):
    # 95% of younger inividuals who did not experience side effects
    test_samples.append(randint(13, 64))
    test_labels.append(0)

    # 95% of older inividuals who suffered from side effects
    test_samples.append(randint(64, 100))
    test_labels.append(1)

test_samples = np.array(test_samples)
test_labels = np.array(test_labels)

test_samples, test_labels = shuffle(test_samples, test_labels)

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_test_samples = scaler.fit_transform(test_samples.reshape(-1, 1))

preds = model.predict(x=scaled_test_samples, batch_size=10)
print(preds)
