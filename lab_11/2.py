import psycopg2

name = input('Enter name you want insert...\n')
phonee = input('Enter phone you want insert...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Y3rbolat_tb'
)
cur = conn.cursor()


'''
create or replace procedure inserting(name varchar, phonee varchar)
as 
$$
begin
    insert into phonebook(username, phone) values ($1, $2);
end;
$$ language plpgsql;
'''
cur.execute(f'call inserting({name}, {phonee})')


cur.close()
conn.commit()
conn.close()