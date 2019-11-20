from tensorflow import keras

def make_model():
    model = keras.Sequential([
        keras.layers.Flatten(input_shape=(54, 6)),
        keras.layers.Dense(10000, activation='relu'),
        keras.layers.Dense(5000, activation='relu'),
        keras.layers.Dense(5000, activation='relu'),
        keras.layers.Dense(3000, activation='relu'),
        keras.layers.Dense(12, activation='softmax')
    ])

    model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy']
              )
    return model