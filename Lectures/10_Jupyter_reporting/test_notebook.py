#!/usr/bin/env python
# coding: utf-8

# # Mise en production ARMA
# 
# Ce notebook est un test pour la mise en production de la génération d'une série process AR.
# 
# Le modèle AR a plusieurs paramètres a determiner. Nous nous limitons à la modification des paramètres suivants:
# 
# - mu
# - rho
# 
# ## Parametrage
# 
# Pour mettre en production le notebook, nous avons besoin d'avoir les librarie suivantes installées: 
# 
# - papermil : https://github.com/nteract/papermill/
# - jupytext : https://github.com/mwouts/jupytext
# - https://medium.com/capital-fund-management/automated-reports-with-jupyter-notebooks-using-jupytext-and-papermill-619e60c37330
# 
# Il est possible de configurer un fichier requirement:
# 
# ```
# # Notebook dependencies
# 
# # Tools used in the article
# jupytext>=1.2
# papermill>=1.2
# nbconvert>=5.5
# jupyter_core>=4.5
# 
# # TOC extension for Binder
# jupyter_contrib_nbextensions
# 
# ```
# 
# Il faut parametrer le notebook avec Jupytext afin de générerer automatiquement les markdowns dans une optique de versioning
# 
# ## Ligne de commande
# 
# Pour utiliser en production le notebook, il suffit d'utiliser la ligne de commande suivante
# 
# ```
# type test_notebook.md | \
#  jupytext --from md --to ipynb --set-kernel - | \
#   papermill -p p 0.5 -p mu 0.5 -p start_date 1/1/2019 | \
#    jupyter nbconvert --stdin --output test_notebook.html
# ```
# 
# Sinon lancer le fichier python `auto.py`. Le fichier genère automatiquement un dS et utilise la date du jour pour la date de valuation.

# In[2]:


import ARMA
import pandas as pd


# ## Parametre AR
# 
# Pour générer une time serie avec un processus AR d'ordre un, il faut renseigner le mu et le rho. Il faut aussi renseigner la date de début. On va générer par defaut 500 dates
# 
# Il faut changer 
# 
# - `p`
# - `mu`
# - `start_date`
# 
# A noter que la cellule ci dessous est une cellule par defaut. Papermill générer une nouvelle cellule en dessus avec les nouvelles valeurs.

# In[7]:


p = 0.8
mu = 0.8
start_date = '1/1/2019'


# In[4]:


AR = ARMA.AR(p = p, mu= mu, lenght = 500)


# In[5]:


date_ = pd.date_range(start=start_date, periods=500)
date_


# In[6]:


df_ar = pd.DataFrame(AR, index =date_)
df_ar.head()


# In[8]:


df_ar.plot.line(y = 'y')


# ## Statistique

# In[ ]:


import seaborn as sns

cm = sns.light_palette("green", as_cmap=True)


# In[ ]:


df_ar.assign(month = lambda x:x.index.month, 
            year = lambda x:x.index.year).groupby('month').agg({
    'y':['min','max', 'mean']
}).style.background_gradient(cmap=cm)

