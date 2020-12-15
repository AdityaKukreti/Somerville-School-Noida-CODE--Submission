import mysql.connector

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def add_account():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
   
    name = input('Enter Name :')
    addr = input('Enter address ')
    phone = input('Enter Phone no :')
    email = input('Enter Email :')
    aadhar = input('Enter AAdhar no :')
    actype = input('Account Type (saving/current ) :')
    balance = input('Enter opening balance :')
    sql = 'insert into customer(name,address,phone,email,aadhar_no,acc_type,balance,status) values ( "' + name +'","'+ addr+'","'+phone+'","'+email+'","'+aadhar+'","'+actype+'",'+balance+',"active" );'
    #print(sql)
    cursor.execute(sql)
    conn.close()
    print('\n\nNew customer added successfully')
    wait= input('\n\n\n Press any key to continue....')
