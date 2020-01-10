import numpy as np
from datetime import date
import sys,os
sys.path.append('/Users/thomas/Google Drive/Projects/Data_science/GitHub/' \
'Repositories/PythonTeaching/Lectures/Tutos_Python/05_Jupyter_reporting')



p = round(np.random.rand(1)[0], 3)
mu = round(np.random.rand(1)[0], 3)

today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

date_ = "{}{}{}".format(d1[:2], d1[3:5], d1[6:])
d1

command = 'cat test_notebook.md | \
 jupytext --from md --to ipynb --set-kernel - | \
  papermill -p p {0} -p mu {1} -p start_date {2} | \
   jupyter nbconvert --stdin --output "Reporting/AR_process{0}_{3}.html"'.format(
   p,
   mu,
   d1,
    date_)



print(command)

os.system(command)
