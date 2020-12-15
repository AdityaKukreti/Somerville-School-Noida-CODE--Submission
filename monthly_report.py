import mysql.connector
from datetime import date

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def clear():
    for _ in range(65):
        print()

def monthly_report():
    clear()

    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    today = date.today()
    cursor = conn.cursor()
    sql = 'select tid,dot,amount,type,acno from transaction t where month(dot)="' + \
        str(today).split('-')[1]+'";'
    cursor.execute(sql)
    records = cursor.fetchall()
    clear()
    print(sql)
    print('Monthly Report :', str(today).split(
        '-')[1], '-,', str(today).split('-')[0])
    print('-'*120)
    for record in records:
        print(record[0], record[1], record[2], record[3], record[4])
    print('-'*120)

    conn.close()
    wait = input('\n\n\n Press any key to continue....')
