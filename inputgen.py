import cupy as np

def generate_inputs(batch_size):
    # Generate random inputs
    inputs = np.random.randint(1, 999_999_999, size=(batch_size, batch_size))
    # Normalize the inputs
    inputs_norm = inputs - np.min(inputs)
    inputs_norm = inputs / (np.max(inputs) - np.min(inputs))
    return inputs_norm
