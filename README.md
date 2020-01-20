# TP de bases de données

Cf. `base.py` pour commencer.

## Création des tables

    c.execute("CREATE TABLE IF NOT EXISTS film (id INTEGER PRIMARY KEY, titre TEXT, annee TEXT, id_realisateur INT)")
	c.execute("CREATE TABLE IF NOT EXISTS realisateur (id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT)")
	c.execute("CREATE TABLE IF NOT EXISTS acteur (id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT)")
	c.execute("CREATE TABLE IF NOT EXISTS jeu (id_film INTEGER, id_acteur INTEGER)")
	c.execute("CREATE TABLE IF NOT EXISTS utilisateur (id INTEGER PRIMARY KEY, prenom TEXT, nom TEXT)")
	c.execute("CREATE TABLE IF NOT EXISTS entree (id_utilisateur INTEGER, id_film INTEGER, note INTEGER)")

Répondez aux questions suivantes.

## Films sortis en 1994
## Films de Christopher Nolan
## Films avec Natalie Portman
## Acteurs de Inception
## Les dix années les plus prospères
## Les dix réalisateurs les plus bankables
## Les dix acteurs les plus bankables
## Les acteurs ayant tourné dans au moins deux films à succès depuis 2010
## Les couplages réalisateur-acteur les plus fréquents
## La note moyenne de chaque utilisateur dans l'ordre alphabétique (nom puis prénom)
## Les dix films les mieux notés
