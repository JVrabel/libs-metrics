import numpy as np
from sklearn.metrics import mutual_info_score

def euclid(a, b):
    return np.linalg.norm(a - b)

def cosine(a, b):
    return 1 - np.dot(a, b) / np.linalg.norm(a) / np.linalg.norm(b)

def direct_mutual_information(x, y, bins=100):
    c_xy, _, _ = np.histogram2d(x, y, bins)
    return - mutual_info_score(None, None, contingency=c_xy)

def mutual_information(a, b, bins=100):
    hgram, _, _ = np.histogram2d(a, b, bins=bins)
    pxy = hgram / float(np.sum(hgram))
    px = np.sum(pxy, axis=1)
    py = np.sum(pxy, axis=0)
    px_py = px[:, None] * py[None, :]
    nzs = pxy > 0
    return - np.sum(pxy[nzs] * np.log(pxy[nzs] / px_py[nzs]))