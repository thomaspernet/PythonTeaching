import xlwings as xw
import numpy as np
import matplotlib.pyplot as plt



def hello_xlwings():
    wb = xw.Book.caller()
    wb.sheets[0].range("A1").value = "Hello xlwings!"


@xw.func
def hello(name):
    return "hello {0}".format(name)

@xw.func
@xw.arg('x', doc='This is x.')
@xw.arg('y', doc='This is y.')
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)


@xw.func
@xw.ret(expand='table')
def dynamic_array(r, c):
    return np.random.randn(int(r), int(c))


@xw.func
def myplot(n):
    sht = xw.Book.caller().sheets.active
    fig = plt.figure()
    x = np.arange(-n, n, 0.1)
    plt.plot(1 / (1 + np.exp(-x)))
    sht.pictures.add(fig, name='MyPlot', update=True)
    return 'Plotted sigmoid function with n={}'.format(n)
