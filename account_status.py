import mysql.connector

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def account_status(acno):
    conn = mysql.connector.connect(host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    sql ="select status,balance from customer where acno ='"+acno+"'"
    result = cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result
