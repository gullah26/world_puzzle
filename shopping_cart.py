"""module exit the program when called"""
import sys


# create a title function
def title():
    print("""\n                         $$$$$$$$$$$$$""")
    print("""                                 $$$$""")
    print("""        Shopping Cart  V1.0     $$$$""")
    print("""                               $$$$""")
    print("""       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$""")


title()

name = input("\n           Enter your name: ")
print("\n      ---------------------------------------------")
print(f"      Hello {name}, welcome to your shopping cart ")
print("      ---------------------------------------------")
print("\n       <<< Press Enter to access menu >>>    ")
input("...")

myCart = []


# funtion that returns the user to the menu
def dash_board():
    while True:
        print("""  <<<<<<<< OPTION MENU >>>>>>>> """)
        print("""  ****************************""")
        print("""  Press 1 - 6 to select option""")
        print("""  ****************************""")
        print("     1: Add item")
        print("     2: View cart")
        print("     3: Search item")
        print("     4: Delete item")
        print("     5: Empty cart  ")
        print("     6: Exit app ""\n")
        option = input("Select option: ")
        if option == "1":
            print("\n    =========================")
            print("    <<  Add item to Cart  >>")
            print("    =========================""\n")
            add_item()
        elif option == "2":
            print("\n    =========================")
            print("    <<      View cart    >>  ")
            print("    =========================""\n")
            view_cart()
        elif option == "3":
            print("\n     =========================")
            print("     <<    Search item   >>")
            print("     =========================""\n")
            search_item()
        elif option == "4":
            print("\n     =========================")
            print("     <<       Delete item   >>")
            print("     =========================""\n")
            delete_item()
        elif option == "5":
            print("\n     =========================")
            print("     <<      Empty cart     >>")
            print("     =========================""\n")
            empty_cart()
        elif option == "6":
            print("\n     =========================")
            print("     <<     Exit program    >>")
            print("     =========================""\n")
            print("Press Enter to Exit")
            input()
            sys.exit(" **** Thank you for your time ***")
        else:
            print("Invalid option selected, RETRY!!!")
            print("Press enter to Return to Menu")
            input()


# function to Add items to the shopping cart
def add_item():
    item = input("\nAdd item to cart: ")
    myCart.append(item.title())
    print()
    print(f"____{item} added to cart____""\n")
    print("\nPress Enter to return to Menu")
    input(".......")


# displays the list of items in the cart
def view_cart():
    print()
    print(f"   Total item(s) in your cart is : {len(myCart)} ""\n")
    for item in myCart:
        print(item)
        break
    else:
        print("\n____!!!Your shopping cart is empty____""\n")
        print("\nPress Enter to return to Menu")
        input(".......")


# Find item in the cart based on user input
def search_item():
    item = input("Find item in cart: ")
    if item in myCart:
        print()
        print(f"____{item} is in cart____""\n")
        print("\nPress Enter to return to Menu")
        input(".......")
        dash_board()
    else:
        print(f"____{item} is not in cart____""\n")
        print("\nPress Enter to return to menu")
        input(".......")


# Finds and delete an item from the cart based on user input
def delete_item():
    item = input("Find item to delete from cart: ")
    if item in myCart:
        myCart.remove(item)
        print(f"\n____{item} deleted from cart____""\n")
        print("\nPress Enter to return to Menu")
        input(".......")
        dash_board()
    else:
        print("\n____No Item deleted____""\n")
        print("\nPress Enter to try again")
        input(".......")


# Empty the cart
def empty_cart():
    print("\nThis will erase all items in the cart")
    answer = input("\nPress y to erase cart or n to return to menu: ")
    if answer == "y":
        print("\n____All item(s) in cart deleted____""\n")
        print("Press enter to return to Menu")
        input(".......")
        dash_board()
    elif answer == "n":
        print("Press enter to return to Menu")
        dash_board()
    else:
        print("\nPress enter to return to Menu")
        input("........")
        dash_board()


dash_board()