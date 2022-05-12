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
	per record;
begin
    for per in select * from phone_  where phone like '+7%' or phone like '8%'
        loop
            insert into phonebook(username, phone) values (per.username, per.phone);
        end loop;

end;  
$$ 
'''
cur.execute("select * from phone_ where phone like '+7%' and phone like '8%';")
not_cor_data = cur.fetchall()
print(not_cor_data)



cur.close()
conn.commit()
conn.close()