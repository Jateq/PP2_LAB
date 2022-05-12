import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='Y3rbolat_tb'
)

cursor = conn.cursor()

username = input()
phone = input()


sql = '''
     UPDATE phonebook
     SET username=%s WHERE number=%s;
     '''

cursor.execute(sql, (username, phone))
conn.commit()

cursor.close()
conn.close()