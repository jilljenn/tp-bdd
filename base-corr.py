import sqlite3
conn = sqlite3.connect('films.db')

c = conn.cursor()

print('# Films sortis en 1994')
for titre, in c.execute('SELECT titre FROM film WHERE annee = 1994'):
	print(titre)
print()

print('# Films de Christopher Nolan')
for titre, in c.execute('SELECT titre FROM film, realisateur WHERE id_realisateur = realisateur.id AND nom = "Nolan"'):
	print(titre)
print()

print('# Films avec Natalie Portman')
for titre, in c.execute('SELECT titre FROM film, jeu, acteur WHERE film.id = id_film AND id_acteur = acteur.id AND prenom = "Natalie"'):
	print(titre)
print()

print('# Acteurs de Inception')
for prenom, nom in c.execute('SELECT prenom, nom FROM film, jeu, acteur WHERE film.id = id_film AND id_acteur = acteur.id AND titre = "Inception"'):
	print(prenom, nom)
print()

print('# Les dix années les plus prospères')
for annee, n in c.execute('SELECT annee, COUNT(annee) n FROM film GROUP BY annee ORDER BY n DESC LIMIT 10'): # COUNT(annee) n == COUNT(annee) AS n
	print(annee, n)
print()

print('# Les dix réalisateurs les plus bankables')
for prenom, nom, n in c.execute('SELECT prenom, nom, COUNT(id_realisateur) n FROM film, realisateur WHERE id_realisateur = realisateur.id GROUP BY id_realisateur ORDER BY n DESC LIMIT 10'): # Piège : si on oublie WHERE id_realisateur = realisateur.id, ça devient aberrant
	print(prenom, nom, n)
print()

print('# Les dix acteurs les plus bankables')
for prenom, nom, n in c.execute('SELECT prenom, nom, COUNT(id_acteur) n FROM film, jeu, acteur WHERE film.id = id_film AND id_acteur = acteur.id GROUP BY id_acteur ORDER BY n DESC LIMIT 10'):
	print(prenom, nom, n)
print()

print('# Les acteurs ayant tourné dans au moins deux films à succès depuis 2010') # Différence entre WHERE (avant GROUP BY) et HAVING (après GROUP BY)
for prenom, nom, n in c.execute('SELECT prenom, nom, COUNT(id_acteur) n FROM film, jeu, acteur WHERE film.id = id_film AND id_acteur = acteur.id AND annee >= 2010 GROUP BY id_acteur HAVING n >= 2'):
	print(prenom, nom, n)
print()

print('# Les couplages réalisateur-acteur les plus fréquents') # Boss level : triple jointure, quadruple GROUP BY
for prenom_r, nom_r, prenom_a, nom_a, n in c.execute('SELECT realisateur.prenom, realisateur.nom, acteur.prenom, acteur.nom, COUNT(*) n FROM film, realisateur, acteur, jeu WHERE id_realisateur = realisateur.id AND film.id = id_film AND id_acteur = acteur.id GROUP BY realisateur.prenom, realisateur.nom, acteur.prenom, acteur.nom ORDER BY n DESC LIMIT 10'):
	print(prenom_r, nom_r, 'avec', prenom_a, nom_a, n)
print()

print('# La moyenne de chaque utilisateur dans l\'ordre alphabétique (nom puis prénom)') # Double ORDER BY
for prenom, nom, note in c.execute('SELECT prenom, nom, AVG(note) FROM utilisateur, entree WHERE id = id_utilisateur GROUP BY id ORDER BY nom, prenom'):
	print(prenom, nom, note)
print()

print('# Les dix films les mieux notés')
for titre, moyenne in c.execute('SELECT titre, AVG(note) moyenne FROM film, entree WHERE film.id = id_film GROUP BY titre ORDER BY moyenne DESC LIMIT 10'):
	print(titre, moyenne)

conn.close()
