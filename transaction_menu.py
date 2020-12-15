from deposit_amount import deposit_amount
from withdraw_amount import withdraw_amount


def clear():
    for _ in range(65):
        print()


def transaction_menu():
    while True:
        clear()
        print(' Trasaction Menu')
        print("\n1.  Deposit Amount")
        print('\n2.  WithDraw Amount')
        print('\n3.  Back to Main Menu')
        print('\n\n')
        choice = int(input('Enter your choice ...: '))
        if choice == 1:
            deposit_amount()
        if choice == 2:
            withdraw_amount()
        if choice == 3:
            break
