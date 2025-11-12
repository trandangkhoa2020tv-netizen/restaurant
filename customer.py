from menu_order import order_food, orders

def customer_menu(customer):
    while True:
        print("\n=== MENU KHÁCH HÀNG ===")
        print("1. Đặt món")
        print("2. Xem đơn hàng")
        print("0. Thoát")
        c = input("Chọn: ")
        if c == "1":
            order_food(customer)
        elif c == "2":
            for o in orders:
                if o["customer"] == customer.name:
                    print(o)
        else:
            break
