from restaurant_objects import *
from restaurant_login import login

def sign_out():
    value = messagebox.askyesno('Confirm','Do you really want to sign out?')
    if value == True:
        os.remove(os.getcwd() + '/csv and text files/restaurant_info.txt')

        frame_1.place_forget()
        frame_2.place_forget()
        frame_3.place_forget()
        frame_4.place_forget()

        ord_delivered_button.place_forget()
        order_pending_label.place_forget()
        delivered_orders_label.place_forget()
        rest.title('The Food Vault Restaurant')
        login()

        

        canvas_2.place_forget()
