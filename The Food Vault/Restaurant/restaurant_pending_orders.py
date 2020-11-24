from restaurant_objects import *

def pen_ord():
    pending_order_button.config(bg = '#c3fff6')
    delivered_order_button.config(bg = 'white')

    delivered_orders_label.place_forget()
    frame_3.place_forget()
    frame_4.place_forget()


    def ord_del():

        cur.execute("UPDATE `user orders` SET `status` = 'Delivered' WHERE `order id` = %s",(pending_orders_treeview.item(pending_orders_treeview.focus())['values'][0],))
        db.commit()

        frame_2.place_forget()

        for i in pending_orders_treeview.get_children():
            pending_orders_treeview.delete(i)

        cur.execute("SELECT `order id`,`customer name`,`date`,`time` FROM `user orders` WHERE `restaurant name` = %s and `status` = 'pending'",(rest_name,))
        count = 0
        for i in cur:
            pending_orders_treeview.insert(parent = '', text = '', index = END, iid = count, values = i)
            count += 1

        


    def open_det(event):


        for i in pending_order_details_treeview.get_children():
            pending_order_details_treeview.delete(i)

        ord_id = pending_orders_treeview.item(pending_orders_treeview.focus())['values'][0]

        cur.execute('SELECT * FROM `user orders` WHERE `order id` = %s',(ord_id,))

        for i in cur:
            items = i[6].split(',')
            items.pop()
            quantities = i[7].split(',')
            quantities.pop()
            prices = i[8].split(',')
            prices.pop()

            customer_name = i[2]
            customer_number = i[3]
            customer_address = i[4]
            restaurant_name = i[5]
            amt_payable = 0
            

        for i in range(len(items)):
            pending_order_details_treeview.insert(parent = '', text = '', iid = i, index = END, values = (items[i],quantities[i],prices[i]))
            amt_payable += int(prices[i]) * int(quantities[i])

        amt_payable = amt_payable + (amt_payable * 18/100)



        frame_2.place(relx = 0.5, rely = 0, relheight = 1, relwidth = 0.5)

        customer_name_entry_1 = Entry(frame_2, width = 28, font = 'Arial 15')
        customer_name_entry_1.insert(END, customer_name)
        customer_name_entry_1.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_name_entry_1.place(relx = 0.4, rely = 0.2)


        customer_number_entry_1 = Entry(frame_2, width = 28, font = 'Arial 15')
        customer_number_entry_1.insert(END, customer_number)
        customer_number_entry_1.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_number_entry_1.place(relx = 0.4, rely = 0.26)


        customer_address_entry_1 = Entry(frame_2, width = 28, font = 'Arial 15')
        customer_address_entry_1.insert(END, customer_address)
        customer_address_entry_1.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_address_entry_1.place(relx = 0.4, rely = 0.32)


        restaurant_name_entry_1 = Entry(frame_2, width = 28, font = 'Arial 15')
        restaurant_name_entry_1.insert(END, restaurant_name)
        restaurant_name_entry_1.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        restaurant_name_entry_1.place(relx = 0.4, rely = 0.38)

        amt_payable_entry_1 = Entry(frame_2, width = 28, font = 'Arial 15')
        amt_payable_entry_1.insert(END, 'Rs ' + str(amt_payable))
        amt_payable_entry_1.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        amt_payable_entry_1.place(relx = 0.4, rely = 0.775)

        frame_2_5.place(relx = 0.05, rely = 0.45, relheight = 0.3, relwidth = 0.86)

    order_pending_label.place(relx = 0.04, rely = 0.1)
    frame_1.place(relx = 0.04, rely = 0.22, relwidth = 0.45, relheight = 0.4)

    for i in pending_orders_treeview.get_children():
        pending_orders_treeview.delete(i)

    with open(os.getcwd() + '/csv and text files/restaurant_info.txt','rb') as f:
        pickle.load(f)
        rest_name = decrypt(pickle.load(f))
    
    rest.title(rest_name)

    cur.execute("SELECT `order id`,`customer name`,`date`,`time` FROM `user orders` WHERE `restaurant name` = %s and `status` = 'pending'",(rest_name,))
    count = 0
    for i in cur:
        pending_orders_treeview.insert(parent = '', text = '', index = END, iid = count, values = i)
        count += 1

    ord_delivered_button.config(command = ord_del)
    ord_delivered_button.place(relx = 0.2, rely = 0.7, relheight = 0.07, relwidth = 0.125)

    canvas_2.place(relx = 0.1, rely = 0.82, relheight = 0.07, relwidth = 0.8)


    pending_orders_treeview.bind('<Double-1>', open_det)
