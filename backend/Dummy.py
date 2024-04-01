import numpy as np

def generate_dummy_stream():
    # Generate continious dummy data
    minval, maxval=1, 100
    data = np.random.randint(minval, maxval+1) # Dummy data
    return data

generate_dummy_stream()

