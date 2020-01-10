# Instruction Documentation Python

Sphinx est une librairie pour générer automatiquement la documentation de vos codes. La documentation officielle pour Sphinx se trouve ici [](https://pythonhosted.org/an_example_pypi_project/sphinx.html)

Premièrement, il faut installer la librarie.

```
conda install -c anaconda sphinx
```

## Generation quickstart

Sphinx a une commande magique pour créer la plupart des documents nécéssaires pour générer le fichier HTML. Veuillez ouvrir Anaconda Prompt et allez dans le repertoire ou vous souhaitez générer la doc.

Lorsque vous êtes dans le répertoire de travail, collez le code suivant `sphinx-quickstart`. Vous devez répondre à plusieurs questions:

- 1: `Separate source and build directories (y/n) [n]: y`
- 2: `Project name: MyFirstDoc`
- 3: `Author name(s): Thomas`
- 4: `Project release []: 0.01`
- 5:  `Project language [en]: en`

Le répertoire de travail a maintenant deux nouveaux dossiers, build et source.

## Format docstring

Pour générer la documentation depuis les fonctions, vous devez respecter le format docstring. La documentation officielle explique le format officiel.

Exemple docstring pour une fonction python:

```
def standardized(X):
    """
        **Standardize Vector**

        This return the standardized values of a given vector

        Args:
            X (float):  Vector to be standardize.

        Returns:
            int.  The return code::
                vector

    """
    X_s = (X - np.mean(X)) / np.std(X)

    return X_s
```

## Modification `conf.py`

Le code quickstart crée un fichier python `conf.py` que vous devez modifez un minimum pour générer la doc. Le fichier se trouve dans source.

Ouvrez le et décommentez:

```
import os
import sys
sys.path.insert(0, os.path.abspath('./..'))
```

Dans la partie extension, ajoutez dans les crochets:

```
['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
```

Le fichier peut contenir d'autres éléments pour améliorer le design du fichier html. Plus d'information [ici](https://pythonhosted.org/an_example_pypi_project/sphinx.html#conf-py)

## génération index

Dans le dossier source, il y a un fichier index. Vous pouvez le modifier afin d'ajouter des éléments, parties, sous-parties, etc.

Pour ajouter le descriptif des fonctions présentent dans le module `standardize`, veuillez coller avant la partie indices and table, les lignes suivantes:

```
Standardize
=====================
.. automodule:: standardize
   :members:
```

## generation fichier html

La façon la plus simple de générer le fichier html est d'utliser le code suivant: `make html`

Le fichier html est disponible dans `docs/build/html/index.html`. Si le fichier ne semble pas à la hauteur de vos esperances, vous pouvez utiliser `make clean` pour supprimer le contenu du dossier build et recommencer.
