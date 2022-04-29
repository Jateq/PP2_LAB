import psycopg2
from config import params

db = psycopg2.connect(**params)

current = db.cursor()
current.execute('SELECT version();')
db_version = current.fetchall()

print(db_version)

current.close()
db.close()