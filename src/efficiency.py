import numpy as np

def efficiency(x, calibration, p=1e-2, x0=250):
    mask = calibration - x0
    return np.where(mask > 0, x * (1 - np.exp(- p * mask)), 0)