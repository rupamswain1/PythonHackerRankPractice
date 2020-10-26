import mysql.connector
#Setup mysql and code: https://www.youtube.com/watch?v=WDEyt2VHpj4&list=PLsyeobzWxl7poL9JTVyndKe62ieoN-MZ3&index=77
mydb=mysql.connector.connect(host="localhost",user="root", passwd="pheonix",database="python")
mycursor=mydb.cursor()
mycursor.execute("create table first(sno int(3), name varchar(40))")
mycursor.execute('insert into first values(1,"try"),(2,"Success")')
mycursor.execute("select * from first")
result=mycursor.fetchall()
for i in result:
    print(i)

mycursor.execute("drop table first")