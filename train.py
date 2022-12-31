import tensorflow as tf
import datasetgen
import inputgen
import model as nn
import cupy as np

model = nn.create_model_for_training()

x = inputgen.generate_inputs(nn.get_batch_size()).get()
y = datasetgen.generate_dataset(nn.get_batch_size()).get()
indices = np.arange(x.shape[0])
np.random.shuffle(indices)
x = x[indices.get()]
y = y[indices.get()]

model.fit(x, y, epochs=5_550, batch_size=nn.get_batch_size())
model.save('xaml-stylegen.h5')