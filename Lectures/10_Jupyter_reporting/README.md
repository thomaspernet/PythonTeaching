# Jupyter_reporting

L'objectif de cette session est d'apprendre a générer automatiquement des documents HTML avec un template réalisé sur Jupyter notebook.

Pour avoir une idée du résultat obtenu, veuillez vous rendre a cette [adresse](TO CHANGE).

Pour utiliser `conda`, pensez a mettre a jour le fichier config et d'ajouter les variables dans l'environement de variables. Veuillez vous référer à ce tutorial pour ajouter des variables

```
conda config --set remote_read_timeout_secs 1000
conda config --set ssl_verify false
```

### Jupytex

Jupytex permet de générer automatiquement des fichiers markdown ou Rmarkdown après chaque sauvegarde du notebook. Le versioning est plus lisible via un fichier texte plutot qu'un notebook.

```
conda install -c conda-forge jupytext
```

### papemill

Papermill est une libraire donnant la possibilité à l'utilisateur d'executer un notebook automatiquement. Certains paramètres dans le notebook peuvent etre mise à jour automatiquement dans le but de mettre à jour les nouvelles valeurs

```
conda install -c conda-forge papermill
```

## generation HTML

L'idée de cette session est de générer un fichier HTML ([exemple](CHANGE.HTML)).

### Config Jupytex

Pour cela, veuillez ouvrir le notebook test_notebook.ipynb (depuis [ici](TO_CHANGE/05_Jupyter_reporting/test_notebook.ipynb)). Le notebook est déjà rédigé, il ne reste plus qu'à configurer Jupytex et papermill.

Si jupytex est installé correctement, vous devriez voir un onglet jupytex dans File. Jupytex donne la possibilité de sauvegarder un notebook dans un des formats suivants:  markdown ou Rmarkdown. Choisissez markdown

![](Introduction_Python/blob/master/images/Jupyter_reporting/1.png?raw=true)

### Config Papermill

Après avoir configuré Jupytex, il faut définir les cellules contenants les paramètres à mettre à jour.

Il faut ajouter un tag aux cellules devant être modifiées. Pour activer le tagging, allez dans View, puis Cell Toolbar et enfin Tag

![](Introduction_Python/blob/master/images/Jupyter_reporting/2.png?raw=true)

Chaque cellule peut maintenant donner lieu a un tagging

![](Introduction_Python/blob/master/images/Jupyter_reporting/3.png?raw=true)

Dans le cadre de notre session, nous allons modifier uniquement la cellule contenant les valeurs `p`, `mu` et `start_date`.

Cliquez à gauche de `Ajouter un mot-clé` puis inscrivez `parameters`.

![](Introduction_Python/blob/master/images/Jupyter_reporting/4.png?raw=true)

Le notebook est maintenant prêt a être mis en production. Pour générer le fichier HTML avec la mise à jour des valeurs, vous pouvez utiliser la ligne de commande ci-desssous. Par defaut, les valeurs de `p`, `mu` et `start_date` sont égales à 0.5,0.5 et 01/01/2019. Pour modifier les valeurs, changer la ligne suivante: ` p 0.5 -p mu 0.5 -p start_date 1/1/2019`

Pour Mac et Linux `cat` pour Windows `type`

```
cat test_notebook.md | jupytext --from md --to ipynb --set-kernel - | papermill -p p 0.5 -p mu 0.5 -p start_date 1/1/2019 | jupyter nbconvert --stdin --output "Reporting/AR_param.html"
```

Il est possible de convertir dans d'autre format via pandoc

```
pandoc AR_process0.508_04112019.html -o AR_process0.508_04112019.docx
```

Un script python est disponible [ici](Introduction_Python/blob/master/05_Jupyter_reporting/auto.py) pour lancer automatiquement le notebook avec des valeurs générer aléatoirements:

```
python auto.py
```

### Pas a Pas

Pour comprendre la ligne de code défini plus haut, vous pouvez lancer pas à pas chaque ligne ci-dessous.

```
jupytext test_notebook.md --set-kernel - --execute

jupytext test_notebook.ipynb --set-kernel -

papermill test_notebook.ipynb test_notebook.ipynb -p p 0.5 -p mu 0.5 -p start_date 1/1/2019

jupyter nbconvert test_notebook.ipynb --to html
```
