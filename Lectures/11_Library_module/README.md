# Modules and Packages

In this tutorial, you will learn how to create a simple python module and a package.

In programming, a module is a piece of software that has a specific functionality. For example, in our example, we will create a python file containing 2 functions to create an AR and MA process, and
another module would be responsible for calling the functions and run them. Each module is a different file, which can be edited separately.

## Writing modules

### Importing modules

Creating a python module is prety much straightforward. Modules in Python are simply Python files with a .py extension. The name of the module will be the name of the file. A Python module can have a set of functions, classes or variables defined and implemented. In the example above, we will have two files, we will have:

myFirstModule/
myFirstModule/ARMA.py
myFirstModule/test_ARMA.py

The Python script ARMA.py will implement the Ar and MA rocess. It will use the function `AR` and `MA` from the file ARMA.py

Modules are imported from other modules using the import command. In this example, the test_ARMA.py script may look something like this:

```
import ARMA

def main():
    AR = ARMA.AR()
    print(AR)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()

```

The `ARMA` module may look something like this:

```
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def AR(p = 0.8, mu= 0.8, lenght = 10):
    """
    process AR: yt = μ + γyt−1 + ϵt

    Autoregressive (AR) models are models in which the value of a variable
    in one period is related to its values in previous periods.

    Parameters:
    p (int): Value of γ
    mu (int): Value of μ

    Returns:
    dict:Returning value of x and y following a AR model of order 1
    """
    list_y =[]
    yt_1 = np.random.normal()
    for i in range(0, lenght):
        et = np.random.normal()
        yt = mu + p*yt_1 + et
        yt_1 = yt
        list_y.append(yt)

    x = np.linspace(0, 10, lenght)
    dic_ = {
    'y': list_y,
    'x':x
    }

    return dic_

  ```

In this example, the test_ARMA module imports the ARMA module, which enables it to use functions implemented in that module. The main function would use the local function AR to run the AR process. To use the function AR from the ARMA module, we would need to specify in which module the function is implemented, using the dot operator. To reference the ARMA function from the test_ARMA module, we would need to import the ARMA module and only then call ARMA.AR().

When the import ARMA directive will run, the Python interpreter will look for a file in the directory which the script was executed from, by the name of the module with a .py prefix, so in our case it will try to look for ARMA.py. If it will find one, it will import it. If not, he will continue to look for built-in modules.

To run the code, go to the folder directory and paste the following code `python test_ARMA.py`: The output should look like:

```
{'y': [0.25730152246319615, 0.023759311056731347, 2.923640484137679, 2.4873472194044606, 2.6346294079575485, 3.447693480615446, 2.4167745314762987, 2.868145500721725, 2.2037589571704874, 2.994596267948448], 'x': array([ 0.        ,  1.11111111,  2.22222222,  3.33333333,  4.44444444,
        5.55555556,  6.66666667,  7.77777778,  8.88888889, 10.        ])}
```

### Writing modules

We may also import the function AR directly into the main script's namespace, by using the `from` command.

You may have noticed that in this example, ARMA does not precede with the name of the module it is imported from, because we've specified the module name in the import command.

The advantages of using this notation is that it is easier to use the functions inside the current module because you don't need to specify which module the function comes from. However, any namespace cannot have two objects with the exact same name, so the import command may replace an existing object in the namespace.

```
from ARMA import AR

def main():
    AR_ = AR()

    print(AR_)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
```

## Writing class

In this session, we will learn how to write a python library. Packages are namespaces which contain multiple packages and modules themselves. They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called `__init__.py`. This file can be empty, and it indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

For the aim of the tutorial, we will code a library to price a structured product using a Heston model.

### Picking A Name

Python module/package names should generally follow the following constraints:

- All lowercase
- Unique on pypi, even if you don’t want to make your package publicly available (you might want to specify it privately as a dependency later)
- Underscore-separated or no word separators at all (don’t use hyphens)

### Creating The Scaffolding

First, create a folder called `myFirstLibrary`. In this folder, we will add the codes to price the product, and the `__init__.py`

myFirstLibrary/
       heston93.py
       __init__.py

## Brief word about heston93
### Heston 93 model

In finance, the Heston model, named after Steven Heston, is a mathematical model describing the evolution of the volatility of an underlying asset. It is a stochastic volatility model: such a model assumes that the volatility of the asset is not constant, nor even deterministic, but follows a random process.

Objective:

- Compute Random path with MC simulation

### Basic Heston model

The basic Heston model assumes that $S_t$, the price of the asset, is determined by a stochastic process.

### Parameter of the model

- Heston parameters
- Kappa:
- Theta:
- Sigma:
- Rho:
- V0:
- OIS:
- Dividend:
- Spot:
- current date:
- valuation date:

## Heston Class

A Class is like an object constructor, or a "blueprint" for creating objects.

### The __init__() Function

To understand the meaning of classes we have to understand the built-in __init__() function.

All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created

Here is an example of an __init__() from the Heston93 class.

```
class heston:
    def __init__(self):
        self.seed = np.random.RandomState(123456)
        self.iteration = 10000
```

### The self Parameter

The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

Here is an example of the `self`. Since we only have two current instance in the class, we only need to use it for those two particulars variables.

```
def RPMC(self, kappa, theta, sigma, rho, dVt, ois, dividend, dS,
  current_date, valuation_date):
      """
      """
      ds_ = (np.ones((self.iteration,1)) * dS).flatten()
      dv_ = (np.ones((self.iteration,1)) * dVt).flatten()
```

The full code is available here.

You can try the class by using this code:

```
import sys,os
sys.path.append('C:\\Users\\X196663\\Documents\\GitHub\\tutorials\\library\\myFirstLibrary')

import heston93 as hs

heston_cal  = hs.heston()

heston_cal.RPMC(kappa=0.5485872,
theta= 0.0462418,
sigma=0.2252450,
rho=-0.5014077 ,
dVt = 0.0190355,
ois = 0.00144,
dividend =  0.02,
dS = 105.42,
current_date= "29/06/2018",
valuation_date =  "19/01/2021")
```
