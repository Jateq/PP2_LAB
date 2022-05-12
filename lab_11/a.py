import csv, psycopg2
conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Y3rbolat_tb'
)

cursor = conn.cursor()
arr = []

with open('a.csv') as f:
    reader = csv.reader(f, delimiter=',')
    
    for row in reader:
        arr.append(row)

sql = '''
    INSERT INTO phone_
    VALUES (%s, %s) RETURNING *;
'''

for row in arr:
    cursor.execute(sql, row)

final = cursor.fetchall()
print(final)