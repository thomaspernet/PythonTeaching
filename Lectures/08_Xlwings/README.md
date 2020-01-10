# Librarie `xlwings`

Dans cette session, nous allons apprendre à utiliser la librarie `xlwings`. `xlwings` est une librarie permettant d'utiliser la puissance de Python/R directement dans Excel.

Les deux atouts majeurs de la librairie sont:

- Import/export de data dans Excel via python
- Utilisation de User Defined Function (UDF) codée en Python/R directement dans Excel.

Xlwings est une librarie Python, et est installée par defaut avec Anaconda. Pour utiliser pleinement les capactités d'`xlwings`, il faut au préalable configurer votre machine.

Noter que si votre objectif consiste a utiliser Python pour importer/exporter des datas dans Excel, aucune configuration n'est recquise. Si, au contraire, vous souhaitez intégrer à votre Excel les UDF codées en Python ou R, alors il faut suivre les étapes ci-desous.

## Configuration Ruban Excel

Le tutorial officiel pour l'Installation du ruban est disponible [ici](https://xlwings.readthedocs.io/en/0.16.0/addin.html#xlwings-addin). Le ruban est un addin a ajouter dans Excel afin de pouvoir utiliser les UDF Python/R dans les spreadsheets.

Tout d'abord, téléchargez l'addin avec cette commande `xlwings addin install`. Attention, Excel doit etre fermé. En ouvrant Excel, vous devriez voir un nouveau ruban. Ensuite, cliquez sur le ruban `developpeur` puis `compléments Excel`. Il faut ajouter le fichier `xlam` depuis le bouton `Parcourir`. Le fichier `xlam` se trouve:

```
C:\Users\USERNAME\AppData\Roaming\Microsoft\Excel\XLSTART
```

Il faut donc pointer le `complément Excel` vers ce dossier. Pour cela, cliquez sur `Parcourir` et trouvez le fichier `xlwings.xlam` dans le repertoire spécifié ci-dessus. Xlwings est maintenant ajoutée a vos Compléments.

Pour supprimer le complément: `xlwings addin remove`

## Configuration `rpy2`

La configuration pour utiliser les UDF R dans Excel via `xlwings` est légèrement plus compliquée. R doit bien sur être installé sur votre machine. Si cela n'est pas le cas, installez le via conda:  `conda install -c r r`. Pour les packages essentiels de R, `conda install -c r r-essentials`

Tout d'abord, il faut télécharger la librarie `rpy2`: `conda install -c r rpy2`. Si cela ne marche pas avec Conda, alors utilisez le fichier binaire `pip install rpy2-2.9.5-cp36-cp36m-win_amd64.whl`.

Il faut maintenant définir plusieurs variables dans les variables d'environement. Ouvrez les variables d'environemen et ajoutez:

```
Nom variable: R_HOME
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Lib\R

Nom variable: R_USER
C:\Users\USERNAME

Nom variable: R_LIBS_USER
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Lib\site-packages
```

Pour savoir si la configuration est correcte, ouvrez n'importe quel IDE Python et tapez `import rpy2.robjects as robjects`. Si la librairie s'importe sans problème, c'est que tout est ok. En cas de problème, essayez d'ajouter les variables suivantes dans le **Path**. Pensez a redémarrer la machine.

```
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Library\mingw-w64\lib
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Library\mingw-w64\bin
C:\Users\USERNAME\AppData\Local\Continuum\anaconda3\Lib\R\bin\x64
```
