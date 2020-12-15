import mysql.connector

with open('mysql_credentials.txt','r') as f:
    a = f.readlines()
    h = a[0].split('=')[-1]
    d = a[1].split('=')[-1]
    u = a[2].split('=')[-1]
    p = a[3].split('=')[-1]
    

def clear():
    for _ in range(65):
        print()


def activate_account():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    clear()
    acno = input('Enter customer Account No :')
    sql = 'update customer set status="active" where acno ='+acno+';'
    cursor.execute(sql)
    print('\n\nAccount Activated')
    wait = input('\n\n\n Press any key to continue....')
