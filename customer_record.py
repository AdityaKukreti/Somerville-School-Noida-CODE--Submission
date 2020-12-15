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


def customer_record():
    conn = mysql.connector.connect(host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    sql ="select * from customer;"
    cursor.execute(sql)
    results = cursor.fetchall()
    clear()
    print('Customer Records')
    print('-'*120)
    for result in results:
        print(result[0], result[1], result[2], result[3], result[4], result[5],result[6], result[7], result[8])
    print('-'*120)
    conn.close()
    wait = input('\n\n\n Press any key to continue....')
