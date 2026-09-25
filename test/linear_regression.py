import numpy as np

def multiple_linear_regression(x, y, z):
    n = len(x)
    
    A = np.array(
        [[n,np.sum(x),np.sum(y)],
        [np.sum(x), np.sum(x**2), np.sum(x*y)],
        [np.sum(y), np.sum(x*y), np.sum(y**2)]]
    )
    
    b = np.array([[np.sum(z)], [np.sum(x*z)], [np.sum(y*z)]])
    
    a = np.linalg.solve(A,b)
    
    return a