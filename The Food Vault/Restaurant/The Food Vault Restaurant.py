from restaurant_objects import *
from restaurant_login import login
from restaurant_pending_orders import pen_ord
from restaurant_delivered_orders import del_ord
from restaurant_sign_out import sign_out


label.place(relheight = 1, relwidth = 1)

canvas_1.place(relx = 0.1, rely = 0.1, relheight = 0.7, relwidth = 0.8)


pending_order_button.config(command = pen_ord)
delivered_order_button.config(command = del_ord)
sign_out_button.config(command = sign_out)

if os.path.isfile(os.getcwd() + '/csv and text files/restaurant_info.txt') == True:
    pen_ord()
else:
    login()


def on_closing():
    global rem_info
    if os.path.isfile(os.getcwd() + '/csv and text files/restaurant_info.txt') == True:
        with open(os.getcwd() + '/csv and text files/restaurant_info.txt','rb') as f:
            for i in range(3):
                rem_info = pickle.load(f)
    ch = messagebox.askokcancel('Quit','Are you sure you want ot quit?')
    if ch == True:
        if rem_info == '0':
            try:
                os.remove(os.getcwd() + '/csv and text files/restaurant_info.txt')
            except FileNotFoundError:
                pass

        rest.destroy()

rest.protocol("WM_DELETE_WINDOW", on_closing)


rest.mainloop()