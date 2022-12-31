import tensorflow as tf

BATCH_SIZE = 10

def create_model_for_training():
    model = tf.keras.models.Sequential([
        # The input layer expects an array of shape (batch_size, 10).
        tf.keras.layers.Dense(units=64, input_shape=(None, 10)),
        tf.keras.layers.Activation('relu'),

        # The first hidden layer has 64 units.
        tf.keras.layers.Dense(units=64),
        tf.keras.layers.Activation('relu'),

        # The second hidden layer has 64 units.
        tf.keras.layers.Dense(units=64),
        tf.keras.layers.Activation('relu'),

        # The output layer has 35 units.
        tf.keras.layers.Dense(units=36),
    ])
    model.compile(optimizer='adam', loss='mae', metrics=['accuracy'])
    return model

def load_model(model_fp):
    model = tf.keras.models.load_model(model_fp)
    return model

def get_batch_size():
    return BATCH_SIZE