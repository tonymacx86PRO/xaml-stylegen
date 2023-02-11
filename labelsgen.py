import cupy as np
import model as nn
import uuid
import log
import sys

# How to use: labelsgen.py

# This module is used to generate a labels file baseline for tweaking and training

def generate_labels(labels_size):
    labels = np.zeros((labels_size, 36))

    # Background (Min: 0, Max: 255)
    labels[:, 0] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 1] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 2] = np.random.randint(0, 255, size=(labels_size,))

    # Foreground (Min: 0, Max: 255)
    labels[:, 3] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 4] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 5] = np.random.randint(0, 255, size=(labels_size,))

    # FontSize (Min: 6, Max: 24)
    labels[:, 6] = np.random.randint(6, 25, size=(labels_size,))

    # FocusVisualStyle (Min: 0, Max: 1)
    labels[:, 7] = np.random.randint(0, 2, size=(labels_size,))

    # BorderBrush (Min: 0, Max: 255)
    labels[:, 8] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 9] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 10] = np.random.randint(0, 255, size=(labels_size,))

    # BorderThickness (Min: 1, Max: 12)
    labels[:, 11] = np.random.randint(1, 13, size=(labels_size,))

    # Button.IsFocused (Min: 0, Max: 1)
    labels[:, 12] = np.random.randint(0, 2, size=(labels_size,))

    # BorderThickness (Button.IsFocused) (Min: 1, Max: 12)
    labels[:, 13] = np.random.randint(1, 13, size=(labels_size,))

    # BorderBrush (Button.IsFocused) (Min: 0, Max: 255)
    labels[:, 14] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 15] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 16] = np.random.randint(0, 255, size=(labels_size,))

    # Button.IsEnabled (Min: 0, Max: 1)
    labels[:, 17] = np.random.randint(0, 2, size=(labels_size,))

    # Background (Button.IsEnabled) (Min: 0, Max: 255)
    labels[:, 18] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 19] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 20] = np.random.randint(0, 255, size=(labels_size,))

    # BorderBrush (Button.IsEnabled) (Min: 0, Max: 255)
    labels[:, 21] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 22] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 23] = np.random.randint(0, 255, size=(labels_size,))

    # Rounding (Min: 0, Max: 1)
    labels[:, 24] = np.random.randint(0, 2, size=(labels_size,))

    # CornerRadius (Rounding) (Min: 2, Max: 16)
    labels[:, 25] = np.random.randint(2, 17, size=(labels_size,))

    # Button.MouseEnter (Min: 0, Max: 1)
    labels[:, 26] = np.random.randint(0, 2, size=(labels_size,))

    # To (Button.MouseEnter)  (Min: 0, Max: 255)
    labels[:, 27] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 28] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 29] = np.random.randint(0, 255, size=(labels_size,))

    # Duration (seconds - Button.MouseEnter) (Min: 0.20, Max: 1.5)
    labels[:, 30] = np.random.uniform(0.20, 1.5, size=(labels_size,))

    # Button.MouseLeave (Min: 0, Max: 1)
    labels[:, 31] = np.random.randint(0, 2, size=(labels_size,))

    # To (Button.MouseLeave) (Min: 0, Max: 255)
    labels[:, 32] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 33] = np.random.randint(0, 255, size=(labels_size,))
    labels[:, 34] = np.random.randint(0, 255, size=(labels_size,))

    # Duration (seconds - Button.MouseLeave) (Min: 0.20, Max: 1.5)
    labels[:, 35] = np.random.uniform(0.20, 1.5, size=(labels_size,))
    labels = labels.round(decimals=2)

    return labels

def arr2csv(arr, file):
    return np.savetxt(f'labels\\{file}.csv', arr, '%5.2f', delimiter=', ', 
    header='Background, Foreground, FontSize, FocusVisualStyle, BorderBrush, BorderThickness, Button.IsFocused, BorderThickness (Button.IsFocused), BorderBrush (Button.IsFocused), Button.IsEnabled, Background (Button.IsEnabled), BorderBrush (Button.IsEnabled), Rounding, CornerRadius (Rounding), Button.MouseEnter, To (Button.MouseEnter), Duration (seconds - Button.MouseEnter), Button.MouseLeave, To (Button.MouseLeave), Duration (seconds - Button.MouseLeave)',
    comments='')

def csv2arr(name):
    return np.loadtxt(f"labels\\{name}.csv", delimiter=',', skiprows=1)


if __name__ == "__main__":
    argv = sys.argv

    log.info("Starting labels baseline generator")
    labels = generate_labels(nn.get_batch_size())
    labels_name = uuid.uuid4()
    labels_json = arr2csv(labels, str(labels_name))
    
    log.info(f"Generated labels: \n{labels}")
    log.info(f"Generated labels shape: {labels.shape}")
    log.info('You have generated a csv example of labels, now refer to the nn-structure.md file to edit your labels. \nThen use it to train NN.')
