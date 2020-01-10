import xlwings as xw
import numpy as np
import rpy2.robjects as robjects
from rpy2.robjects import numpy2ri
# you might want to use some relative path or place the file in R's current working dir
import os

r_path  = 'https://sgithub.fr.world.socgen/raw/X196663/xlwings/master/r_file.R'
#print(relative_path)
robjects.r.source(r_path)

@xw.func
def myfunction(x, y):
    myfunc = robjects.r['myfunction']
    return tuple(myfunc(x, y))


numpy2ri.activate()

@xw.func
@xw.arg("x", np.array, ndim=2)
@xw.arg("y", np.array, ndim=2)
def array_function(x, y):
    array_func = robjects.r['array_function']
    return np.array(array_func(x, y))
