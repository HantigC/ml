import numpy as np

def generate_6_clusters():
    a = np.random.multivariate_normal([10, 10], [[1, 0], [0, 1]], 300)
    b = np.random.multivariate_normal([5, 0], [[1, 0], [0, 1]], 200)
    c = np.random.multivariate_normal([5, 10], [[1, 0], [0, 1]], 200)
    d = np.random.multivariate_normal([10, 0], [[1, 0], [0, 1]], 100)
    e = np.random.multivariate_normal([15, 0], [[1, 0], [0, 1]], 200)
    f = np.random.multivariate_normal([15, 10], [[1, 0], [0, 1]], 200)
    x = np.r_[a, b, c, d, e, f]
    return x