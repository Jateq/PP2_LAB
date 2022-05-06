import psycopg2

namee = input('Enter name you need...\n')

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
)

cur = conn.cursor()

'''
create or replace function getRecord(namee text)
    returns record as
$$
    declare 
        person record;
begin
    select * into person from PhoneBook1 where phonebook1.name = $1;
    return person;
end; 
$$
LANGUAGE plpgsql;
'''

cur.execute("SELECT  getRecord( %s); ",(namee,))
result = cur.fetchone()
print(result)



cur.close()
conn.commit()
conn.close()