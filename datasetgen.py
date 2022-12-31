import cupy as np

def generate_dataset(dataset_size):
    dataset = np.zeros((dataset_size, 36))

    # Background (Min: 0, Max: 255)
    dataset[:, 0] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 1] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 2] = np.random.randint(0, 255, size=(dataset_size,))

    # Foreground (Min: 0, Max: 255)
    dataset[:, 3] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 4] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 5] = np.random.randint(0, 255, size=(dataset_size,))

    # FontSize (Min: 6, Max: 24)
    dataset[:, 6] = np.random.randint(6, 25, size=(dataset_size,))

    # FocusVisualStyle (Min: 0, Max: 1)
    dataset[:, 7] = np.random.randint(0, 2, size=(dataset_size,))

    # BorderBrush (Min: 0, Max: 255)
    dataset[:, 8] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 9] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 10] = np.random.randint(0, 255, size=(dataset_size,))

    # BorderThickness (Min: 1, Max: 12)
    dataset[:, 11] = np.random.randint(1, 13, size=(dataset_size,))

    # Button.IsFocused (Min: 0, Max: 1)
    dataset[:, 12] = np.random.randint(0, 2, size=(dataset_size,))

    # BorderThickness (Button.IsFocused) (Min: 1, Max: 12)
    dataset[:, 13] = np.random.randint(1, 13, size=(dataset_size,))

    # BorderBrush (Button.IsFocused) (Min: 0, Max: 255)
    dataset[:, 14] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 15] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 16] = np.random.randint(0, 255, size=(dataset_size,))

    # Button.IsEnabled (Min: 0, Max: 1)
    dataset[:, 17] = np.random.randint(0, 2, size=(dataset_size,))

    # Background (Button.IsEnabled) (Min: 0, Max: 255)
    dataset[:, 18] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 19] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 20] = np.random.randint(0, 255, size=(dataset_size,))

    # BorderBrush (Button.IsEnabled) (Min: 0, Max: 255)
    dataset[:, 21] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 22] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 23] = np.random.randint(0, 255, size=(dataset_size,))

    # Rounding (Min: 0, Max: 1)
    dataset[:, 24] = np.random.randint(0, 2, size=(dataset_size,))

    # CornerRadius (Rounding) (Min: 2, Max: 16)
    dataset[:, 25] = np.random.randint(2, 17, size=(dataset_size,))

    # Button.MouseEnter (Min: 0, Max: 1)
    dataset[:, 26] = np.random.randint(0, 2, size=(dataset_size,))

    # To (Button.MouseEnter)  (Min: 0, Max: 255)
    dataset[:, 27] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 28] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 29] = np.random.randint(0, 255, size=(dataset_size,))

    # Duration (seconds - Button.MouseEnter) (Min: 0.20, Max: 1.5)
    dataset[:, 30] = np.random.uniform(0.20, 1.5, size=(dataset_size,))

    # Button.MouseLeave (Min: 0, Max: 1)
    dataset[:, 31] = np.random.randint(0, 2, size=(dataset_size,))

    # To (Button.MouseLeave) (Min: 0, Max: 255)
    dataset[:, 32] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 33] = np.random.randint(0, 255, size=(dataset_size,))
    dataset[:, 34] = np.random.randint(0, 255, size=(dataset_size,))

    # Duration (seconds - Button.MouseLeave) (Min: 0.20, Max: 1.5)
    dataset[:, 35] = np.random.uniform(0.20, 1.5, size=(dataset_size,))

    return dataset