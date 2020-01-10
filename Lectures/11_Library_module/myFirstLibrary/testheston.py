import sys,os
sys.path.append('/Users/thomas/Google Drive/Projects/Data_science/' \
'GitHub/Repositories/PythonTeaching/Lectures/Tutos_Python/' \
'04_Library_module/myFirstLibrary')

os.getcwd()

import heston93 as hs

heston_cal  = hs.heston(current_date = "29/06/2018")

print(heston_cal.RPMC(kappa=0.5485872,
theta= 0.0462418,
sigma=0.2252450,
rho=-0.5014077 ,
dVt = 0.0190355,
ois = 0.00144,
dividend =  0.02,
dS = 105.42,
valuation_date =  "19/01/2021"))
