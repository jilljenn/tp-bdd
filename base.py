import sqlite3
conn = sqlite3.connect('films.db')

c = conn.cursor()

print('# 5 films au hasard')
for titre, in c.execute('SELECT titre FROM film ORDER BY RANDOM() LIMIT 5'):
	print(titre)

conn.close()
