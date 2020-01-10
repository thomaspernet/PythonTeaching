
import pandas as pd
import numpy as np


class DATA:
    def __init__(self, first_date, shape):
        self.first_date = first_date
        self.shape = shape

    def create_dataframe(self):
        """
        """
        df_dates = pd.date_range(
            self.first_date,
             periods=self.shape,
              freq='W-WED')

        dup_ts = pd.Series(np.random.random(self.shape), index=df_dates)

        return dup_ts

    def create_dataframe_1(self, first_date, shape):
        """
        """
        df_dates = pd.date_range(
            first_date,
             periods=shape,
              freq='W-WED')

        dup_ts = pd.Series(np.random.random(shape), index=df_dates)

        return dup_ts

    def printdate(self):
        """
        """
        print(self.first_date)
