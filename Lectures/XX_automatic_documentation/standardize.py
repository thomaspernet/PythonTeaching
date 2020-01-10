"""Standardize Toolbox Functions

.. moduleauthor:: Thomas <thomas.pernet-coudrier-ext>

"""

import numpy

def standardized(X):
    """
        **Standardize Vector**

        This return the standardized values of a given vector

        Args:
            X (float):  Vector to be standardize.

        Returns:
            int.  The return code::
                vector

    """
    X_s = (X - np.mean(X)) / np.std(X)

    return X_s

def min_max(X):
    """
        **Normalize Vector**

        This return the normalized values of a given vector

        Args:
            X (float):  Vector to be Normalize.

        Returns:
            int.  The return code::
                vector

    """
    X_n = (X - np.min(X)) / (np.max(X) - np.min(X))

    return X_n

def log_scale(X):
    """
        **Log scale Vector**

        This return the log values of a given vector

        Args:
            X (float):  Vector to be in log.

        Returns:
            int.  The return code::
                vector

    """
    X_l = np.log(X)

    return X_l
