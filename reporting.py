import sqlite3
conn = sqlite3.connect('store')

cursor = conn.execute("SELECT name,owner,species,sex,checkups,birth,death from pet")

for row in cursor:
   print("name = ", row[0])
   print("owner = ", row[1])
   print("species = ", row[2])
   print("sex = ", row[3])
   print("checkups = ", row[4])
   print("birth = ", row[5])
   print("death = ", row[6], "\n")
