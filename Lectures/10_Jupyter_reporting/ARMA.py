# -*- coding: utf-8 -*-
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


def MA(q = 0.8, mu = 4, lenght = 10):
    """
    Process MA: yt = μ + ϵt + θϵt−1
    Parameters:
    p (int): Value of γ
    mu (int): Value of μ

    Moving average (MA) models account for the possibility of a relationship
     between a variable and the residuals from previous periods

    Returns:
    dict:Returning value of x and y following a MA model of order 1
    """
    list_y =[]
    et_1 = 0
    for i in range(0, lenght):
        et = np.random.normal()
        yt = mu + et + q* et_1
        et_1 = et
        list_y.append(yt)
    ### Plot result
    x = np.linspace(0, 10, lenght)
    dic_ = {
        'y': list_y,
        'x':x
    }

    return dic_
