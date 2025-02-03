import sqlite3
conn = sqlite3.connect('store')

cursor = conn.execute("UPDATE pet SET death = '2024-12-13' WHERE name = 'Fluffy' AND owner = 'Harold'")
cursor = conn.execute("UPDATE pet SET death = '2024-12-11' WHERE name = 'Claws' AND owner = 'Gwen'")

conn.commit()