import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Y3rbolat_tb'
)

cursor = conn.cursor()

username = input()

sql = '''
     DELETE FROM phonebook
     WHERE username = %s;
     '''

cursor.execute(sql, (username,))
conn.commit()

cursor.close()
conn.close()