import labelsgen
import inputgen
import model as nn
import numpy as np
import uuid
import sys
import log

# How to use: train.py <labels file> <training epochs> <optional: model name>

# Getting all arguments from terminal
argv = sys.argv

# Creating the model structure
model = nn.create_model_for_training()

# Generating some random input (features) x
x = inputgen.generate_inputs(nn.get_batch_size())

# Using existing labels from argv[1] (labels) y
y = []
if not len(argv) > 1:
    log.error("The first required argument is missing: the name of the labels file without extension in the labels folder")
    sys.exit(1)
else:
    y = labelsgen.csv2arr(argv[1])


#Shuffling our arrays
randomize = np.arange(len(x))
np.random.shuffle(randomize)
x = x[randomize]
y = y[randomize]
x = np.asarray(x.get())
y = np.asarray(y.get())

# Fitting the model
if not len(argv) > 2:
    log.error("The second required argument is missing: how many epochs to train")
    sys.exit(1)
else:
    print('\n')
    model.fit(x, y, epochs=int(argv[2]), batch_size=nn.get_batch_size())
    # Evaluating the model
    model.evaluate(x, y)
    model.summary()

# Saving the fitted model
if not len(argv) > 3:
    model.save(f'models\\{uuid.uuid4}.h5')
else:
    model.save(f'models\\{argv[3]}.h5')