![](doc/board.jpg?raw=true)

# Design III: Atlas18

> Le projet Atlas fait appel au concept de la téléopération d’un robot autonome. Un usager utilise un ordinateur (la station de base) pour acheminer, via un lien sans-fil, une commande de haut niveau au robot situé sur un terrain à distance. Avec ses capacités de perception, de locomotion, de préhension et son intelligence, le robot exécute la tâche demandée sans intervention humaine. Le robot envoie un signal à la station de base pour confirmer la fin de l’exécution de la tâche lorsque celle-ci est complétée.


[![Build Status](https://travis-ci.com/Gabswim/design3-h18.svg?token=oFRzF26Q45xGBoB8qvZi&branch=master)](https://travis-ci.com/Gabswim/design3-h18) [![codecov](https://codecov.io/gh/Gabswim/design3-h18/branch/master/graph/badge.svg?token=qXU5zomZOm)](https://codecov.io/gh/Gabswim/design3-h18)


---

## Table des matières

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Tests](#tests)

---

## Installation

```bash
sudo pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
export PYTHONPATH=$(pwd)/src:$PYTHONPATH
```
Copier votre fichier de propriétés dans ~/.atlas/debug.yml.
```bash
mkdir -p ~/.atlas
cp sample-config/debug-linux.yml ~/.atlas/debug.yml
```


- Pour PyCharm, il faut effectuer cette étape:
![](doc/mark_as_source.png?raw=true) 

---

## Utilisation
### Pour prendre des photos
[voir dossier infra](./infra)


## Tests 
### Structure de fichiers
Dans le dossier `test`, placer les fichiers de test avec un nom qui débute par `test_`. Ne jamais mettre de fichier `__init__.py` dans le dossier test, sinon python devient mêlé. Vos méthodes de test doivent commencer par `test_` sinon, elles ne seront pas exécutées.

### Commandes d'exécution
> Pour effectuer les tests, il faut rouler la commande suivante à la racine du projet. Cette commande donne aussi la couverture des tests.
```bash
sh run_tests.sh
```
> Pour avoir un rapport de couverture de test plus détaillé :
```bash
sh run_coverage.sh
```

---

## Contribuer

### Étape 1

- 👯 Cloner le repo: `https://github.com/Gabswim/design3-h18.git`

### Étape 2

- Créer une branche

### Step 3

- 🔃 Créer un pull request et attendre les vérifications de **Travis**, **Codecov** et un **membre de l'équipe**

---

