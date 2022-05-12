import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Y3rbolat_tb'
)

cur = conn.cursor()

page_current = 2
records_per_page = 4  
offset = (page_current - 1) * records_per_page 

s = "select * from phonebook order by username limit "
s +=  str(records_per_page)
s += " offset " + str(offset)


cur.execute(s)
res = cur.fetchall()
print(res)


cur.close()
conn.commit()
conn.close()