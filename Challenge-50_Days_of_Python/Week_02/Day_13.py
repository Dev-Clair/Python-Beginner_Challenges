# DAY_13: Your VAT

def your_vat():
    """
        Function that enables customers to check an item price after VAT.
    """
    while True:
        item_name = str(input("Enter Item Reference or Name: \t"))
        try:
            basic_price = float(input("\nEnter Item-price: \t"))
            tax = float(input("\nEnter VAT on item: \t"))
            vat = tax/100
        except ValueError:
            print("\nPlease enter the correct item price and VAT\n")
        else:
            item_price = basic_price + (basic_price * vat)
            print(f"\nThe cost of {item_name} is Naira {item_price}\n")
        print("Will you like to re-enter or check for another item? yes or no\n")
        check_another_item = input("\t\tchoice: ").lower()
        if check_another_item == "no":
            break


your_vat()
