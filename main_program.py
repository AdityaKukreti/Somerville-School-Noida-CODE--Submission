import mysql.connector
from datetime import date
from add_account import add_account
from modify_account import modify_account
from close_account import close_account
from activate_account import *
from transaction_menu import transaction_menu
from search_menu import search_menu
from daily_report import daily_report



def clear():
    for _ in range(65):
        print()


def main_menu():
    while True:
      clear()
      print(' Main Menu')
      print("\n1.  Add Account")
      print('\n2.  Modify Account')
      print('\n3.  Close Account')
      print('\n4.  Activate Account')
      print('\n5.  Transaction Menu')
      print('\n6.  Search Menu')
      print('\n7.  Report Menu')
      print('\n8.  Close application')
      print('\n\n')
      choice = int(input('Enter your choice ...: '))
      if choice == 1:
        add_account()
      if choice == 2:
        modify_account()
      if choice == 3:
        close_account()

      if choice == 4:
        activate_account()

      if choice ==5 :
        transaction_menu()
      if choice ==6 :
        search_menu()
      if choice == 7:
        report_menu()
      if choice ==8:
        break

if __name__ == "__main__":
    main_menu()
