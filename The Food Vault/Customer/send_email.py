import smtplib
from email.message import EmailMessage
import pickle
from tkinter import messagebox
import os
from project_objects import db,cur
from project_encryption_and_decryption import *
from project_invoice_creation import *



username = ''
password = ''

with open(os.getcwd() + '/csv and text files/smtp_info.txt','rb') as f:
    username = decrypt(pickle.load(f))
    password = decrypt(pickle.load(f))

smtp = smtplib.SMTP_SSL('smtp.gmail.com')
smtp.login(username,password)

def forgot_password_mail(user_name,user_email,code):
    
    msg = EmailMessage()
    msg['Subject'] = "Hey {name}, it seems that you've forgotten your passsword".format(name = user_name)
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Don't worry, we'll help you with it! </h1>
    <h3> Kindly use the following code for changing your password-</h3>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
    


def verification_code_mail(user_name,user_email,code):


    msg = EmailMessage()
    msg['Subject'] = "Hello {name}, We're glad to have you!".format(name = user_name)
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Welcome to our Community! </h1>
    <h3> Kindly use the following code for verifying your email-</h3>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
        

def email_change_alert_email(user_name,user_email,code):


    msg = EmailMessage()
    msg['Subject'] = "Email change request"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Greetings {user_name}, </h1>
    <h3>We have received an email change request for your account</h3>
    <h4> Kindly use the following code for verifying that it's you-</h4>
    <h4> Your verification code - {code}</h4>
    </p>
    </body>
    </html>
    """.format(code = code, user_name = user_name), subtype = 'html')

    try:
        smtp.send_message(msg)
        return True
    except ConnectionResetError:
        messagebox.showerror('Error','Connection with the server has been forcibly closed. Try restarting your system if error keeps occuring.')
        return False
    

def order_placed_email(ord_id,user_name,user_email):

    file_no = 1

    while True:
        if os.path.isfile(os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf') is True:
            file_no += 1
        else:
            break

    
    cur.execute('SELECT * FROM `user orders` WHERE `order id` = %s',(ord_id,))
    for k in cur:
        order_id = 'Order id - ' + str(k[0])
        name = 'Customer Name - ' + k[2]
        number = 'Customer Number - ' + k[3]
        address = 'Customer Address - ' + k[4]
        rest = 'Restaurant Name - ' + k[5]
        rest_address = 'Restaurant Address - ' + k[-3]
        rest_number = 'Restaurant Number - ' + k[-2]
        ord_time = 'Order Time - ' + str(k[-1])
        item = k[6].split(',')
        item.pop()
        quantity = k[7].split(',')
        quantity.pop()
        price = k[8].split(',')
        price.pop()
        date = 'Order Date - ' + str(k[9])
        total_quantity = 0
        total_price = 0
        for i in range(len(item)):
            total_quantity += int(quantity[i])
            total_price += int(price[i]) * int(quantity[i])


    pdf = FPDF()

    pdf.add_page()


    pdf.set_font('Arial', size = 14)



    pdf.cell(200,10, txt = 'Python Project', ln = 1, align = 'C') 

    pdf.cell(200,5, txt = 'Food Ordering Program', ln = 1, align = 'C')

    pdf.dashed_line(34, 27, 185, 27, dash_length = 1)

    pdf.cell(200,12, txt = 'Invoice', ln = 1, align = 'C')

    pdf.dashed_line(34, 35, 185, 35, dash_length = 1)

    pdf.set_left_margin(33)

    pdf.cell(200,8, txt = order_id, ln = 1, align = 'L')
    pdf.cell(200,7, txt = date, ln = 1, align = 'L')
    pdf.cell(200,7, txt = ord_time, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest_number, ln = 1, align = 'L')
    pdf.cell(200,7, txt = rest_address, ln = 1, align = 'L')
    pdf.cell(200,7, txt = name, ln = 1, align = 'L')
    pdf.cell(200,7, txt = number, ln = 1, align = 'L')
    pdf.cell(200,7, txt = address, ln = 1, align = 'L')

    pdf.dashed_line(34, 110, 185, 110, dash_length = 1)

    pdf.set_y(104)
    pdf.set_x(38)
    pdf.cell(200, 22, txt = 'Item', ln = 1)

    pdf.set_y(104)
    pdf.set_x(120)
    pdf.cell(200, 22, txt = 'Quantity', ln = 1)

    pdf.set_y(104)
    pdf.set_x(160)
    pdf.cell(200, 22, txt = 'Price', ln = 1)

    pdf.dashed_line(34, 120, 185, 120, dash_length = 1)

    

    for i in range(len(item)):
        pdf.set_x(38)
        y = pdf.get_y()
        pdf.cell(200, 10, txt = str(item[i]), ln = 1)



        pdf.set_y(y)
        pdf.set_x(125)
        pdf.cell(200, 10, txt = quantity[i], ln = 1)
        pdf.set_y(y)
        pdf.set_x(162)
        pdf.cell(200, 10, txt = price[i] + '.00', ln = 1)

    pdf.dashed_line(34, pdf.get_y() + 1.5, 185, pdf.get_y() + 1.5, dash_length = 1)

    

    pdf.set_x(38)
    y = pdf.get_y()
    pdf.cell(200, 17, txt = 'Total', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)
    pdf.cell(200,17, txt = str(total_price) + '.00', ln = 1)

    y = pdf.get_y() - 10
    pdf.set_y(y)
    pdf.set_x(38)
    pdf.cell(200, 17, txt = 'GST(18%)', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)
    tax = str(total_price * (18/100))
    fin_tax = ''
    cnt = 0
    for i in tax:
        if i == '.':
            fin_tax = fin_tax + tax[cnt:cnt + 3]
            break
        else:
            fin_tax = fin_tax + i
            cnt += 1

            
    pdf.cell(200, 17, txt = fin_tax, ln = 1)

    pdf.dashed_line(34, pdf.get_y() - 3, 185, pdf.get_y() - 3, dash_length = 1)

    y = pdf.get_y() - 5
    pdf.set_y(y)
    pdf.set_x(38)
    pdf.cell(200, 17, txt = 'Grand Total', ln = 1)
    pdf.set_y(y)
    pdf.set_x(125)
    pdf.cell(200, 17, txt = str(total_quantity), ln = 1)
    pdf.set_y(y)
    pdf.set_x(162)

    fin_tot_0 = str(total_price + float(fin_tax))
    fin_tot = ''
    cnt = 0
    for i in fin_tot_0:
        if i == '.':
            fin_tot = fin_tot + fin_tot_0[cnt:cnt + 3]
            break
        else:
            fin_tot = fin_tot + i
            cnt += 1


    pdf.cell(200,17, txt = fin_tot, ln = 1)

    pdf.dashed_line(34, pdf.get_y() - 3, 185, pdf.get_y() - 3, dash_length = 1)

    pdf.set_x(pdf.get_x() - 20)
    pdf.cell(200,17, txt = 'Thank you for ordering', ln = 1, align = 'C')
    pdf.set_y(pdf.get_y() - 8)
    pdf.set_x(pdf.get_x() - 20)
    pdf.cell(200,17, txt = 'We hope you have a great day!', ln = 1, align = 'C')

    file_name = os.getcwd() + '/Invoice/Invoice_' + str(file_no) + '.pdf'
    pdf.output(name = file_name)



    msg = EmailMessage()
    msg['Subject'] = "We have received your order!"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> Your order has been placed successfully!</h1>
    <h3>Hey {user_name}! Thank you for ordering! We hope you enjoy your meal.</h3>
    <h4>Kindly find the order details in the attachements.</h4>
    </p>
    </body>
    </html>
    """.format(user_name = user_name), subtype = 'html')

    msg.add_attachment(open(file_name, "rb").read(), maintype = 'application', subtype = 'octet-stream', filename = 'Invoice.pdf')


    smtp.send_message(msg)

    os.remove(file_name)


def account_deletion_mail(user_name,user_email):

    msg = EmailMessage()
    msg['Subject'] = "Account Deletion"
    msg['From'] = username
    msg['To'] = [user_email]

    msg.add_alternative("""\
    <html>
    <body>
    <p><h1 style = "color:#00c6ff;font-family:verdana""> We're sorry to know that you're leaving. </h1>
    <h3> We'll miss you {user_name}. We hope you stay safe.</h3>
    <h4>Goodbye!</h4>
    </p>
    </body>
    </html>
    """.format(user_name = user_name), subtype = 'html')


    smtp.send_message(msg)

