items={
    "notebook": 75,
    "pen": 20,
    "pencil box": 100, 
    "calculator": 350,
    "geometry box": 250
}
cart={}
def get_quantity():
    while True:
        try:
         quantity=int(input("Enter the quantity: "))
         if quantity>0:
             return quantity
         else:
             print("!!Quantity must be gretater than 0!!\n")
        except ValueError:
            print("!!!!Enter Valid Quantity!!!!\n")
def  show_items():
    print("\nAvailable Items")
    for item,price in items.items():
        print(f"{item.capitalize()} - ₹{price}")
def add_item():
    show_items()
    name=input("Enter name of the item to add: ").strip().lower()
    if name not in items:
        print("Item not available")
        return
    quantity=get_quantity()   
    if name in cart:
        cart[name]+=quantity
    else:
        cart[name]=quantity
    print(f"{name.capitalize()} added to cart.")
def remove_item():
        name=input("Enter name of the item to remove: ").strip().lower()
        if name in cart:
            del cart[name]
            print(f"{name.capitalize()} added removed from cart")
        else:
            print("!!Item not found!!") 
def update_quantity():
        name=input("Enter name of the itame to update the quantity: ").strip().lower() 
        new_quantity=get_quantity()
        cart[name]=new_quantity
        print("Quantity Updated")
def view_cart():
        if not cart:
            print("!!!!Cart is Empty!!!!")
            return
        print("-------Cart Details--------") 
        total=0
        for  item,quantity in cart.items():
            price=items[item]
            item_total=price*quantity
            total+=item_total
            print(f"{item.capitalize()}: \nPrice: ₹{price} \nQuantity: {quantity} \nTotal: ₹{item_total}")
       
        print(f"\nOverall Bill Amount: ₹{total}")    
def menu():
        while True:
         print("\n--------Shopping Menu---------")
         print("1. View Available Items \n2. Add Item to Cart \n3. Remove Item from Cart \n4. Update Quantity of Item \n5. View Cart \n6. Exit")
         choice=input("Enter your selection (1-6): ")
         if choice=="1":
             show_items()
         elif choice=="2":
             add_item()
         elif choice=="3":
             remove_item()
         elif choice=="4":
             update_quantity()
         elif choice=="5":
             view_cart()
         elif choice=="6":
             print("Thank you for shoping")
             break
         else:
             print("!!!!Invalid Selection Try Again!!!!")
menu()                                 
