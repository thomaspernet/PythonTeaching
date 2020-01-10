
# GitHub & Rstudio

Dans ce tutorial, vous allez voir comment connecter GitHub avec Rstudio. Avant toute chose, il est impératif d'avoir Git installé sur la machine. Si cela n'est pas encore fait, veuillez vous référer à ce tutorial.

Le GitHub des RISQ/MOD se trouve à cette adresse: https://sgithub.fr.world.socgen/RISQ-MOD-Retail-Analytics

# Git

Tout d'abord, vous devez localiser l'éxecutable `.exe` Git sur votre machine. Pour cela, ouvrez l'explorateur Windows et écrivez `Git Bash`. Dès que l'icone s'affiche, cliquez dessus

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/0_tuto.PNG?raw=true)


Pour connaitre le path de l'executable, il faut taper `where git`

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/1_tuto.png?raw=true)

Comme vous pouvez le voir, l'executable se trouve dans le path suivant: `C:\Program Files (x86)\Freeware\Git\1.9.5\bin\git.exe`

Maintenant que vous avez récupéré le path, vous pouvez ouvrir Rstudio.

# Rstudio

Si vous n'avez jamais parametré Git dans Rstudio, vous pouvez le faire dans la section `Global options...`. Cette section se trouve dans l'onglet `Tools`.

Lorsque vous avez ouvert `Global options...`, vous pouvez désormais configurer Git avec Rstudio. Il y a trois étapes à réaliser:

1. Cocher `Enable version control interface for Rstudio projects`
2. Indiquer le path de l'executable à partir de `Browse` dans la section `Git executable`

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/2_tuto.png?raw=true)

3. Cocher `Git Bash as shell for Git projects`

Il n'est pas nécéssaire de configuer le SVN puisque vous utilisez Git. La création d'une clé SSH RSA est toutefois indispensable pour faire la connection avec GitHub.

## Clé SSH RSA en local

Pour créer la clé SSH, il suffit de cliquer sur `Create RSA key` et d'indiquer une paraphrase:

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/3_tuto.png?raw=true)

Notez bien le path ou va être généré la clé ainsi que la paraphrase, vous allez en avoir besoin ultérieurement. Pour ma part, la clé a été crée dans ce path `C:\Users\X196663\.ssh` et la paraphrase est `helloworld`.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/4_tuto.png?raw=true)

## Clé SSH RSA dans GitHub

Maintenant que la clé SSH est générée, il faut faire la liaison avec GitHub. Tout d'abord, connectez-vous à votre compte Github Enterprise et rendez-vous sur le paramètrage du compte

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/5_tuto.png?raw=true)

Dans le panel de gauche, vous devez trouver un onglet `SSH and GPG key`. Dans cette onglet, cliquez sur `New SSH key`. C'est dans cette partie que vous allez coller la clé SSH se trouvant en local.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/6_tuto.png?raw=true)

Tout d'abord, donnez un nom à la clé, `MyFirstKey`, puis ouvrez le document `id_rsa.pub` qui se trouve dans le dossier `.ssh`. Vous pouvez l'ouvrir avec le Text Editor

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/7_tuto.png?raw=true)

Copiez l'ensemble du document et collez le dans la partie réservée a cet effet dans GitHub.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/8_tuto.png?raw=true)

La clé est maintenant configurée à la fois dans GitHub et dans Rstudio.

# Projet Git

Il est préférable d'avoir le repo sur GitHub avant de faire la connection avec Rstudio. Avant de continuer, veuillez créer un repo sur GitHub. Dans le cadre de ce tutorial, vous pouvez l'appeler `GitHub_Rstudio` puis récupérer la clé SSH.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/9_tuto.png?raw=true)

## Clone Repo

Dans cette partie, nous allons voir comment cloner le repo `GitHub_Rstudio`

La prcédure se fait en deux étapes:

- Création Projet R avec Git Versioning
- Connection avec la Remote

### Creation projet R

Pour utiliser R et Github, il faut obligatoirement créer un projet. Le projet va contenir le dossier `.git` et l'ensemble des documents nécéssaires au bon déroulement du projet. Tout ce qui se trouve dans le projet va etre envoyé dans la remote, à l'exception des extensions indiquées dans le `.gitignore`

Premiérement, veuillez créer un nouveau projet en cliquant sur `File` puis `New project`

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/10_tuto.PNG?raw=true)

Rstudio vous propose trois options, il faut selectionner la dernière, `Version Control`

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/11_tuto.png?raw=true)

Trois options se présentent de nouveau à vous, veuillez selectionner `Git`.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/12_tuto.png?raw=true)

Comme c'est la première fois que vous faites la liaison, vous devez entrer la paraphrase précédement créée

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/13_tuto.png?raw=true)


Si tout est ok, vous devriez voir deux nouveaux fichiers dans le dossier fraichement cloné:

- `.gitignore`
- `github_test.Proj`

![](https://sgithub.fr.world.socgen/raw/X196663/GitHub_Rstudio/master/Images/14_tuto.png)

Il se peut que Rstudio vous demande de mettre vos identifiants. Allez dans la shell, copiez-collez les lignes suivantes en changeant vos identifiants:

```
git config --global user.name "THOMAS PERNET COUDRIER"
git config --global user.email thomas.pernet-coudrier-ext@socgen.com
```

## Push sur GitHub


Maintenant que vous avez cloné le repo, vous pouvez désormais faire des pull/push depuis Rstudio. Il suffit d'ouvrir le projet contenant le repo en local (i.e `GitHub_Rstudio`) et de cliquer sur l'icon `git` et `commit`.  

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/15_tuto.png?raw=true)


Selectionnez les fichiers que vous souhaitez envoyer dans GitHub. Dans la partie `commit`, indiquez simplement `Add file` puis cliquez sur `commit`. En dernière étape, cliquez sur `Push` pour envoyer dans la remote.

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/16_tuto.png?raw=true)

Pour vérifiez que tout marche, rendez vous sur le repo en ligne, rafraichissez la page puis vous devriez voir les fichiers ajoutées

![](https://sgithub.fr.world.socgen/X196663/Introduction_Python/blob/master/images/rstudio_github/17_tuto.png?raw=true)
