from restaurant_objects import *


def del_ord():      
    delivered_order_button.config(bg = '#c3fff6')
    pending_order_button.config(bg = 'white')

    frame_1.place_forget()
    frame_2.place_forget()
    ord_delivered_button.place_forget()



    def open_det(event):


        for i in delivered_order_details_treeview.get_children():
            delivered_order_details_treeview.delete(i)

        ord_id = delivered_orders_treeview.item(delivered_orders_treeview.focus())['values'][0]

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
            delivered_order_details_treeview.insert(parent = '', text = '', iid = i, index = END, values = (items[i],quantities[i],prices[i]))
            amt_payable += int(prices[i]) * int(quantities[i])

        amt_payable = amt_payable + (amt_payable * 18/100)


        frame_4.place(relx = 0.5, rely = 0, relheight = 1, relwidth = 0.5)

        customer_name_entry_2 = Entry(frame_4, width = 28, font = 'Arial 15')
        customer_name_entry_2.insert(END, customer_name)
        customer_name_entry_2.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_name_entry_2.place(relx = 0.4, rely = 0.2)

        customer_number_entry_2 = Entry(frame_4, width = 28, font = 'Arial 15')
        customer_number_entry_2.insert(END, customer_number)
        customer_number_entry_2.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_number_entry_2.place(relx = 0.4, rely = 0.26)

        customer_address_entry_2 = Entry(frame_4, width = 28, font = 'Arial 15')
        customer_address_entry_2.insert(END, customer_address)
        customer_address_entry_2.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        customer_address_entry_2.place(relx = 0.4, rely = 0.32)

        restaurant_name_entry_2 = Entry(frame_4, width = 28, font = 'Arial 15')
        restaurant_name_entry_2.insert(END, restaurant_name)
        restaurant_name_entry_2.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        restaurant_name_entry_2.place(relx = 0.4, rely = 0.38)

        amt_payable_entry_2 = Entry(frame_4, width = 28, font = 'Arial 15')
        amt_payable_entry_2.insert(END, 'Rs ' + str(amt_payable))
        amt_payable_entry_2.config(state = DISABLED, disabledbackground = 'white', disabledforeground = 'black')
        amt_payable_entry_2.place(relx = 0.4, rely = 0.775)

        frame_4_5.place(relx = 0.05, rely = 0.45, relwidth = 0.86, relheight = 0.3)


    delivered_orders_label.place(relx = 0.04, rely = 0.1)
    frame_3.place(relx = 0.04, rely = 0.22, relwidth = 0.45, relheight = 0.4)

    for i in delivered_orders_treeview.get_children():
        delivered_orders_treeview.delete(i)

    with open(os.getcwd() + '/csv and text files/restaurant_info.txt','rb') as f:
        pickle.load(f)
        rest_name = decrypt(pickle.load(f))

    cur.execute("SELECT `order id`,`customer name`,`date`,`time` FROM `user orders` WHERE `restaurant name` = %s and `status` = 'Delivered'",(rest_name,))
    count = 0
    for i in cur:
        delivered_orders_treeview.insert(parent = '', text = '', index = END, iid = count, values = i)
        count += 1


    delivered_orders_treeview.bind('<Double-1>', open_det)
