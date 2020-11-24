from restaurant_objects import *
from restaurant_pending_orders import *

def login():

    def check_login():
        if rest_code_entry.get() == '':
            messagebox.showerror('Error','Enter your restaurant code')
        elif rest_name_entry.get() == '':
            messagebox.showerror('Error','Enter your restaurant name')
        elif rest_code_entry.get() not in rest_codes:
            messagebox.showerror('Error','No restaurant with this code is registered')
        elif rest_name_entry.get() not in rest_names:
            messagebox.showerror('Error','No restaurant with this name is registered')
        else:
            with open(os.getcwd() + '/csv and text files/restaurant_info.txt','wb') as f:
                pickle.dump(encrypt(rest_code_entry.get()), f)
                pickle.dump(encrypt(rest_name_entry.get()), f)
                pickle.dump(str(rem_info.get()), f)

            login_label.place_forget()
            rest_name_label.place_forget()
            rest_name_entry.place_forget()
            rest_code_label.place_forget()
            rest_code_entry.place_forget()
            rest_login_button.place_forget()
            rem_info_checkbox.place_forget()

            pen_ord()




    login_label.place(relx = 0.35, rely = 0.1)

    rest_code_label.place(relx = 0.27, rely = 0.35)
    rest_code_entry.place(relx = 0.42, rely = 0.35)

    rest_name_label.place(relx = 0.27, rely = 0.45)
    rest_name_entry.place(relx = 0.42, rely = 0.45)

    rem_info_checkbox.place(relx = 0.42, rely = 0.51)

    rest_login_button.config(command = check_login)
    rest_login_button.place(relx = 0.425, rely = 0.65, relheight = 0.06, relwidth = 0.15)

    rest_codes = []
    rest_names = []

    cur.execute('SELECT `rest code`,`rest name` FROM `rest info`')
    for i in cur:
        rest_codes.append(str(i[0]))
        rest_names.append(i[1])
    
    