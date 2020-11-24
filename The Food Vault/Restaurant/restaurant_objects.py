from tkinter import *
from tkinter import messagebox,ttk
import mysql.connector
import os
import pickle
from project_encryption_and_decryption import *

with open(os.getcwd() + '/csv and text files/pass file.txt','rb') as f:
    my_user = decrypt(pickle.load(f))
    my_host = decrypt(pickle.load(f))
    my_pass = decrypt(pickle.load(f))

db = mysql.connector.connect(user = '{username}'.format(username = my_user), host = '{host}'.format(host = my_host), passwd = '{password}'.format(password = my_pass))
cur = db.cursor()


cur.execute('USE project')

rest = Tk()
rest.geometry('1920x1080')
rest.state('zoomed')
rest.iconbitmap(os.getcwd() + '/Background and Icon/vegan-food.ico')
rest.title('The Food Vault Restaurant')
style = ttk.Style()
style.theme_use('clam')

background = PhotoImage(file = os.getcwd() + '/Background and Icon/629222.png') 
label = Label(rest, image = background)


canvas_1 = Canvas(rest, bg = '#34aeeb')
canvas_2 = Canvas(rest, bg = '#34aeeb')


frame_1 = Frame(canvas_1)
frame_2 = Frame(canvas_1, bg = '#34aeeb')
frame_2_5 = Frame(frame_2)


frame_3 = Frame(canvas_1)
frame_4 = Frame(canvas_1, bg = '#34aeeb')
frame_4_5 = Frame(frame_4)

rem_info = IntVar()

rem_info_checkbox = Checkbutton(canvas_1, text = 'Keep me signed in',font = 'Arial 13', variable = rem_info, activebackground = '#34aeeb', bg = '#34aeeb', cursor = 'hand2')

order_pending_label = Label(canvas_1, text = 'Pending Orders', font = 'Arial 20 bold', bg = '#34aeeb')
order_details_label_1 = Label(frame_2, text = 'Order Details', font = 'Arial 20 bold', bg = '#34aeeb')
order_details_label_1.place(relx = 0.05, rely = 0.1)

customer_name_label_1 = Label(frame_2, text = 'Customer Name:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_name_label_1.place(relx = 0.05, rely = 0.2)

customer_number_label_1 = Label(frame_2, text = 'Mobile Number:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_number_label_1.place(relx = 0.05, rely = 0.26)

customer_address_label_1 = Label(frame_2, text = 'Delivery Address:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_address_label_1.place(relx = 0.05, rely = 0.32)

restaurant_name_label_1 = Label(frame_2, text = 'Restaurant Name:', font = 'Arial 15 bold', bg = '#34aeeb')
restaurant_name_label_1.place(relx = 0.05, rely = 0.38)

amt_payable_label_1 = Label(frame_2, text = 'Amount Payable:', font = 'Arial 15 bold', bg = '#34aeeb')
amt_payable_label_1.place(relx = 0.05, rely = 0.775)

delivered_orders_label = Label(canvas_1, text = 'Orders Delivered', font = 'Arial 20 bold', bg = '#34aeeb')
order_details_label_2 = Label(frame_4, text = 'Order Details', font = 'Arial 20 bold', bg = '#34aeeb')
order_details_label_2.place(relx = 0.05, rely = 0.1)



customer_name_label_2 = Label(frame_4, text = 'Customer Name:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_name_label_2.place(relx = 0.05, rely = 0.2)

customer_number_label_2 = Label(frame_4, text = 'Mobile Number:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_number_label_2.place(relx = 0.05, rely = 0.26)

customer_address_label_2= Label(frame_4, text = 'Delivery Address:', font = 'Arial 15 bold', bg = '#34aeeb')
customer_address_label_2.place(relx = 0.05, rely = 0.32)

restaurant_name_label_2 = Label(frame_4, text = 'Restaurant Name:', font = 'Arial 15 bold', bg = '#34aeeb')
restaurant_name_label_2.place(relx = 0.05, rely = 0.38)


amt_payable_label_2 = Label(frame_4, text = 'Amount Payable:', font = 'Arial 15 bold', bg = '#34aeeb')
amt_payable_label_2.place(relx = 0.05, rely = 0.775)


pending_order_button = Button(canvas_2, text = 'Pending Orders', border = 0, bg = 'white', activebackground = '#b3fff6', font = 'Arial 13', cursor = 'hand2')
pending_order_button.place(relx = 0.1, rely = 0.175, relheight = 0.65, relwidth = 0.2)

delivered_order_button = Button(canvas_2, text = 'Delivered Orders', border = 0, bg = 'white', activebackground = '#b3fff6', font = 'Arial 13', cursor = 'hand2')
delivered_order_button.place(relx = 0.4, rely = 0.175, relheight = 0.65, relwidth = 0.2)

sign_out_button = Button(canvas_2, text = 'Sign Out', border = 0, bg = 'white', activebackground = '#c3fff6', font = 'Arial 13', cursor = 'hand2')
sign_out_button.place(relx = 0.7, rely = 0.175, relheight = 0.65, relwidth = 0.2)

login_label = Label(canvas_1, text = 'Restaurant Login', font = 'Arial 30 bold', bg = '#34aeeb')
rest_code_label = Label(canvas_1, text = 'Restaurant Code:', font =  'Arial 15 bold', bg = '#34aeeb')
rest_code_entry = Entry(canvas_1, width = 30, font = 'Arial 15')
rest_name_label = Label(canvas_1, text = 'Restaurant Name:', font = 'Arial 15 bold', bg = '#34aeeb')
rest_name_entry = Entry(canvas_1, width = 30, font = 'Arial 15')



treeview_scrollbar = Scrollbar(frame_1)
treeview_scrollbar.pack(side = RIGHT, fill = Y)

pending_orders_treeview = ttk.Treeview(frame_1, yscrollcommand = treeview_scrollbar.set)
treeview_scrollbar.config(command = pending_orders_treeview.yview)


pending_orders_treeview['columns'] = ('Order id', 'Customer Name', 'Order Date','Order Time')

pending_orders_treeview.column('#0', width = 0, stretch = 0)
pending_orders_treeview.column('Order id',  width = 60, minwidth= 50, anchor = W)
pending_orders_treeview.column('Customer Name', width = 150, minwidth = 100, anchor = W)
pending_orders_treeview.column('Order Date', width = 100, minwidth = 50, anchor = W)
pending_orders_treeview.column('Order Time', width = 100, minwidth = 50, anchor = W)


pending_orders_treeview.heading('#0', text = '', anchor = W)
pending_orders_treeview.heading('Order id', text = 'Order id', anchor = W)
pending_orders_treeview.heading('Customer Name', text = 'Customer Name', anchor = W)
pending_orders_treeview.heading('Order Date', text = 'Order Date', anchor = W)
pending_orders_treeview.heading('Order Time', text = 'Order Time', anchor = W)


treeview_scrollbar_1 = Scrollbar(frame_2_5)
treeview_scrollbar_1.pack(side = RIGHT, fill = Y)

pending_order_details_treeview = ttk.Treeview(frame_2_5, yscrollcommand = treeview_scrollbar_1.set)
treeview_scrollbar_1.config(command = pending_order_details_treeview.yview)

pending_order_details_treeview['columns'] = ('Item','Quantity','Price')

pending_order_details_treeview.column('#0', width = 0, stretch = 0)
pending_order_details_treeview.column('Item', width = 100, minwidth = 50, anchor = W)
pending_order_details_treeview.column('Quantity', width = 60, minwidth = 50, anchor = W)
pending_order_details_treeview.column('Price', width = 60, minwidth = 50, anchor = W)

pending_order_details_treeview.heading('#0', text = '', anchor = W)
pending_order_details_treeview.heading('Item', text = 'Item', anchor = W)
pending_order_details_treeview.heading('Quantity', text = 'Quantity', anchor = W)
pending_order_details_treeview.heading('Price', text = 'Price', anchor = W)

pending_orders_treeview.place(relheight = 1, relwidth = 0.96)
pending_order_details_treeview.place(relheight = 1, relwidth = 0.965)



treeview_scrollbar_2 = Scrollbar(frame_3)
treeview_scrollbar_2.pack(side = RIGHT, fill = Y)

delivered_orders_treeview = ttk.Treeview(frame_3, yscrollcommand = treeview_scrollbar_2.set)
treeview_scrollbar_2.config(command = delivered_orders_treeview.yview)

delivered_orders_treeview['columns'] = ('Order id', 'Customer Name', 'Order Date','Order Time')

delivered_orders_treeview.column('#0', width = 0, stretch = 0)
delivered_orders_treeview.column('Order id',  width = 60, minwidth= 50, anchor = W)
delivered_orders_treeview.column('Customer Name', width = 150, minwidth = 100, anchor = W)
delivered_orders_treeview.column('Order Date', width = 100, minwidth = 50, anchor = W)
delivered_orders_treeview.column('Order Time', width = 100, minwidth = 50, anchor = W)


delivered_orders_treeview.heading('#0', text = '', anchor = W)
delivered_orders_treeview.heading('Order id', text = 'Order id', anchor = W)
delivered_orders_treeview.heading('Customer Name', text = 'Customer Name', anchor = W)
delivered_orders_treeview.heading('Order Date', text = 'Order Date', anchor = W)
delivered_orders_treeview.heading('Order Time', text = 'Order Time', anchor = W)


treeview_scrollbar_3 = Scrollbar(frame_4_5)
treeview_scrollbar_3.pack(side = RIGHT, fill = Y)

delivered_order_details_treeview = ttk.Treeview(frame_4_5, yscrollcommand = treeview_scrollbar_3.set)
treeview_scrollbar_3.config(command = delivered_order_details_treeview.yview)

delivered_order_details_treeview['columns'] = ('Item','Quantity','Price')

delivered_order_details_treeview.column('#0', width = 0, stretch = 0)
delivered_order_details_treeview.column('Item', width = 100, minwidth = 50, anchor = W)
delivered_order_details_treeview.column('Quantity', width = 60, minwidth = 50, anchor = W)
delivered_order_details_treeview.column('Price', width = 60, minwidth = 50, anchor = W)

delivered_order_details_treeview.heading('#0', text = '', anchor = W)
delivered_order_details_treeview.heading('Item', text = 'Item', anchor = W)
delivered_order_details_treeview.heading('Quantity', text = 'Quantity', anchor = W)
delivered_order_details_treeview.heading('Price', text = 'Price', anchor = W)

delivered_orders_treeview.place(relheight = 1, relwidth = 0.96)
delivered_order_details_treeview.place(relheight = 1, relwidth = 0.965)

ord_delivered_button = Button(canvas_1, text = 'Order Delivered', bg = 'white', activebackground = '#c3fff6', border = 0, font = 'Arial 13', cursor = 'hand2')

rest_login_button = Button(canvas_1, text = 'Login', bg = 'white', activebackground = '#b3fff6', border = 0, font = 'Arial 13', cursor = 'hand2')
