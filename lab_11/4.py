# Create procedure to insert many new users by list of name and phone. Use loop and if statement in stored procedure. 
# Check correctness of phone in procedure and return all incorrect data.
    
import psycopg2, re

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'Y3rbolat_tb'
)
cur = conn.cursor()

'''
do
$$
    declare
        student record;
    begin
        for student in select * from phonebook limit 4
            loop
                raise notice 'username = %, phone = %', student.username, student.phone;
            end loop;
    end
$$;
'''
cur.execute("select * from phonebook limit 4")
not_cor_data = cur.fetchall()
print(not_cor_data)