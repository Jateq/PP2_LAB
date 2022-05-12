import psycopg2
conn  = psycopg2.connect(
     host = 'localhost',
     database = 'postgres',
     user = 'postgres',
     password = 'Y3rbolat_tb'
)
cursor = conn.cursor()

username = 'Kanye'
phone = '9'


sql = '''
     INSERT INTO phonebook
     VALUES(%s, %s);
     '''

cursor.execute(sql, (username, phone))
cursor.close()

conn.commit()
conn.close()