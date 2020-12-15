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

def search_menu():
    conn = mysql.connector.connect(
        host=h, database=d, user=u, password=p)
    cursor = conn.cursor()
    while True:
        clear()
        print(' Search Menu')
        print("\n1.  Account No")
        print('\n2.  Aadhar Card')
        print('\n3.  Phone No')
        print('\n4.  Email')
        print('\n5.  Names')
        print('\n6.  Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        field_name=''
    
        if choice == 1:
            field_name ='acno'
    
        if choice == 2:
            field_name ='aadhar_no'
    
        if choice == 3:
            field_name = 'phone'
        
        if choice == 4:
            field_name = 'email'

        if choice == 5:
            field_name = 'name'
        
        if choice == 6:
            break
        msg ='Enter '+field_name+': '
        value = input(msg)
        if field_name=='acno':
            sql = 'select * from customer where '+field_name + ' = '+value+';'
        else:
            sql = 'select * from customer where '+field_name +' like "%'+value+'%";'
        #print(sql)
        cursor.execute(sql)
        records = cursor.fetchall()
        n = len(records)
        clear()
        print('Search Result for ', field_name, ' ',value)
        print('-'*80)
        for record in records:
        print(record[0], record[1], record[2], record[3],
                record[4], record[5], record[6], record[7], record[8])
        if(n <= 0):
            print(field_name, ' ', value, ' does not exist')
        wait = input('\n\n\n Press any key to continue....')

        conn.close()
        wait=input('\n\n\n Press any key to continue....')
