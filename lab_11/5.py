import psycopg2


conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Y3rbolat_tb'
)
cur = conn.cursor()


name = input('Enter username you want delete...\n')


# procedure was created inside pg admin/tools/query tool
'''
create or replace procedure deleting(name varchar)
as
$$
begin
    delete from phonebook where username = $1;
end;
$$
    LANGUAGE plpgsql;

'''
cur.execute(f'CALL deleting(\'{name}\');')


cur.close()
conn.commit()
conn.close()