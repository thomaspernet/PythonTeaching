import numpy as np
from datetime import date
import pandas as pd
from workalendar.europe import France
cal = France()

class heston:
    def __init__(self, current_date):
        self.seed = np.random.RandomState(123456)
        self.iteration = 10000
        self.current_date = current_date

    def date_transformed(self, valuation_date):
        """
        La fonction calcule le nombre de jours avant une date de
        constatation/maturité;
        la date maximum rescale (jour/delta) et la liste des dates rescales
        si elle existe
        Si la liste des valuations_date a une seule valeur, ie la date de
        maturité alors
        le code va dans except
        """
        dDt = 252

        try:
            days_to_T = [
                cal.get_working_days_delta(x, self.current_date) for x in
                 valuation_date
                ]
            days_to_T_scaled = [
                cal.get_working_days_delta(x, self.current_date) / dDt for x in
                 valuation_date
                ]
            T_scale = max(days_to_T_scaled)
            return days_to_T, T_scale, days_to_T_scaled
        except:
            days_to_T = cal.get_working_days_delta(valuation_date,
             self.current_date)
            T_scale = cal.get_working_days_delta(
                valuation_date, self.current_date) / dDt
        return days_to_T, T_scale

    def RPMC(self, kappa, theta, sigma, rho, dVt, ois, dividend, dS,
    valuation_date):
        """
        """
        ds_ = (np.ones((self.iteration,1)) * dS).flatten()
        dv_ = (np.ones((self.iteration,1)) * dVt).flatten()
        list_Ds = []
        list_Dv = []
        dDt = 1/252
        current_date = pd.to_datetime(self.current_date, format = "%d/%m/%Y")
        valuation_date = pd.to_datetime(valuation_date,
		 format = "%d/%m/%Y")

        date_transformed_ = self.date_transformed(valuation_date)
        days = np.array(date_transformed_[0])
        maturity_days = np.max(days)

        for n in range(1, maturity_days + 1):
            Z1 = self.seed.normal(loc=0.0, scale=1.0, size = self.iteration)
            Zt = self.seed.normal(loc=0.0, scale=1.0, size = self.iteration)
            Z2 = rho * Z1 + np.power(1 - np.square(rho),0.5) * Zt

            #Z1, Z2 = Z()
            ds_ = ds_ * (1 + (ois - dividend) * dDt + np.power(dVt * dDt,
             0.5) * Z2)
            dv_ = dv_ + kappa*(theta - dVt) * dDt + sigma * \
                np.power(dv_ * dDt, 0.5) * Z1
            dv_ = np.abs(dv_)

            list_Ds.append(ds_)
            list_Dv.append(dv_)

        ## Compute average last DS
        if n == maturity_days:
            avg = np.mean(ds_)

        return avg
