import cupy as np

def generate_inputs(batch_size):
    # Generate random integers between 1 and 999_999_999
    inputs = np.random.randint(1, 999_999_999, size=(batch_size, batch_size))
    # Normalize the inputs
    inputs_norm = inputs - np.min(inputs)
    inputs_norm = inputs / (np.max(inputs) - np.min(inputs))
    # Return the normalized inputs
    return inputs_norm
