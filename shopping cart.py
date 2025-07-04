

cart = {}

def add_fruit():
    fruit = input("Enter fruit name: ").capitalize()
    price = float(input(f"Enter price per {fruit}: "))
    quantity = int(input(f"Enter quantity of {fruit}: "))
    
    if fruit in cart:
        cart[fruit]['quantity'] += quantity
    else:
        cart[fruit] = {'price': price, 'quantity': quantity}
    
    print(f"{quantity} {fruit}(s) added to cart.\n")

def view_cart():
    if not cart:
        print("Your fruit cart is empty.\n")
        return

    print("🍎 Your Fruit Cart:")
    total = 0
    for fruit, details in cart.items():
        item_total = details['price'] * details['quantity']
        total += item_total
        print(f"{fruit} - R{details['price']} x {details['quantity']} = R{item_total:.2f}")
    print(f"Total: R{total:.2f}\n")

def remove_fruit():
    fruit = input("Enter fruit to remove: ").capitalize()
    if fruit in cart:
        del cart[fruit]
        print(f"{fruit} removed from cart.\n")
    else:
        print(f"{fruit} not found in your cart.\n")

def checkout():
    view_cart()
    print("✅ Checkout complete. Thank you for buying fruits!\n")
    exit()

# Menu Loop
while True:
    print("===== 🍇 Fruit Shopping Cart Menu =====")
    print("1. Add Fruit")
    print("2. View Cart")
    print("3. Remove Fruit")
    print("4. Checkout")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_fruit()
    elif choice == '2':
        view_cart()
    elif choice == '3':
        remove_fruit()
    elif choice == '4':
        checkout()
    elif choice == '5':
        print("👋 Goodbye! Stay healthy with fruits.")
        break
    else:
        print("❌ Invalid choice. Please try again.\n")
