import numpy as np

def abs_area(x):
    """Calculate the area under the absolute values of the given points.
    
    The integral is done using the trapezoid rule.

    Parameters
    ----------
    x : ndarray
        The input points to use for the calculationss

    Returns
    -------
    abs_area : float
        The absolute area under the given points.
    """
    return np.sum(np.abs(x))
