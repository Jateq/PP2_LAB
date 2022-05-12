import psycopg2

name = input('Enter username you need...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Y3rbolat_tb'
)

cur = conn.cursor()

'''
create or replace function record(name varchar)
    returns record
as
$$
declare
    student record;
begin
    select * into student from phonebook where phonebook.username = $1;
    return student;
end; 
$$ language plpgsql;
'''

cur.execute("select record(%s); ",(name,))
result = cur.fetchone()
print(result)

cur.close()
conn.commit()
conn.close()