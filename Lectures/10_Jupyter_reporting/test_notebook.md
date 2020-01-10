---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.1'
      jupytext_version: 1.2.4
  kernel_info:
    name: python3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

<!-- #region {"papermill": {"duration": 0.010459, "end_time": "2019-11-21T17:00:34.044821", "exception": false, "start_time": "2019-11-21T17:00:34.034362", "status": "completed"}, "tags": []} -->
# Mise en production ARMA

Ce notebook est un test pour la mise en production de la génération d'une série process AR.

Le modèle AR a plusieurs paramètres a determiner. Nous nous limitons à la modification des paramètres suivants:

- mu
- rho

## Parametrage

Pour mettre en production le notebook, nous avons besoin d'avoir les librarie suivantes installées: 

- papermil : https://github.com/nteract/papermill/
- jupytext : https://github.com/mwouts/jupytext
- https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330

Il est possible de configurer un fichier requirement:

```
# Notebook dependencies

# Tools used in the article
jupytext>=1.2
papermill>=1.2
nbconvert>=5.5
jupyter_core>=4.5

# TOC extension for Binder
jupyter_contrib_nbextensions

```

Il faut parametrer le notebook avec Jupytext afin de générerer automatiquement les markdowns dans une optique de versioning

## Ligne de commande

Pour utiliser en production le notebook, il suffit d'utiliser la ligne de commande suivante

```
type test_notebook.md | \
 jupytext --from md --to ipynb --set-kernel - | \
  papermill -p p 0.5 -p mu 0.5 -p start_date 1/1/2019 | \
   jupyter nbconvert --stdin --output test_notebook.html
```

Sinon lancer le fichier python `auto.py`. Le fichier genère automatiquement un dS et utilise la date du jour pour la date de valuation.
<!-- #endregion -->

```python papermill={"duration": 0.704483, "end_time": "2019-11-21T17:00:34.755428", "exception": false, "start_time": "2019-11-21T17:00:34.050945", "status": "completed"} tags=[]
import ARMA
import pandas as pd
```

<!-- #region {"papermill": {"duration": 0.005432, "end_time": "2019-11-21T17:00:34.766271", "exception": false, "start_time": "2019-11-21T17:00:34.760839", "status": "completed"}, "tags": []} -->
## Parametre AR

Pour générer une time serie avec un processus AR d'ordre un, il faut renseigner le mu et le rho. Il faut aussi renseigner la date de début. On va générer par defaut 500 dates

Il faut changer 

- `p`
- `mu`
- `start_date`

A noter que la cellule ci dessous est une cellule par defaut. Papermill générer une nouvelle cellule en dessus avec les nouvelles valeurs.
<!-- #endregion -->

```python papermill={"duration": 0.010904, "end_time": "2019-11-21T17:00:34.782146", "exception": false, "start_time": "2019-11-21T17:00:34.771242", "status": "completed"} tags=["parameters"]
p = 0.8
mu = 0.8
start_date = '1/1/2019'
```

```python papermill={"duration": 0.011711, "end_time": "2019-11-21T17:00:34.798437", "exception": false, "start_time": "2019-11-21T17:00:34.786726", "status": "completed"} tags=["injected-parameters"]
# Parameters
p = 0.5
mu = 0.5
start_date = "1/1/2019"

```

```python papermill={"duration": 0.012544, "end_time": "2019-11-21T17:00:34.816051", "exception": false, "start_time": "2019-11-21T17:00:34.803507", "status": "completed"} tags=[]
AR = ARMA.AR(p = p, mu= mu, lenght = 500)
```

```python papermill={"duration": 0.016324, "end_time": "2019-11-21T17:00:34.837500", "exception": false, "start_time": "2019-11-21T17:00:34.821176", "status": "completed"} tags=[]
date_ = pd.date_range(start=start_date, periods=500)
date_
```

```python papermill={"duration": 0.017176, "end_time": "2019-11-21T17:00:34.859620", "exception": false, "start_time": "2019-11-21T17:00:34.842444", "status": "completed"} tags=[]
df_ar = pd.DataFrame(AR, index =date_)
df_ar.head()
```

```python papermill={"duration": 0.240178, "end_time": "2019-11-21T17:00:35.105494", "exception": false, "start_time": "2019-11-21T17:00:34.865316", "status": "completed"} tags=[]
df_ar.plot.line(y = 'y')
```

<!-- #region {"papermill": {"duration": 0.005847, "end_time": "2019-11-21T17:00:35.118053", "exception": false, "start_time": "2019-11-21T17:00:35.112206", "status": "completed"}, "tags": []} -->
## Statistique
<!-- #endregion -->

```python papermill={"duration": 0.076523, "end_time": "2019-11-21T17:00:35.201307", "exception": false, "start_time": "2019-11-21T17:00:35.124784", "status": "completed"} tags=[]
import seaborn as sns

cm = sns.light_palette("green", as_cmap=True)
```

```python papermill={"duration": 0.296319, "end_time": "2019-11-21T17:00:35.503694", "exception": false, "start_time": "2019-11-21T17:00:35.207375", "status": "completed"} tags=[]
df_ar.assign(month = lambda x:x.index.month, 
            year = lambda x:x.index.year).groupby('month').agg({
    'y':['min','max', 'mean']
}).style.background_gradient(cmap=cm)
```
