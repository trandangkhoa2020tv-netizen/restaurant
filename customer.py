# customer.py
from menu_order import order_food, orders, show_menu, search_food

def customer_menu(customer):
    while True:
        print("\n=== MENU KHÁCH HÀNG ===")
        print("1. Xem menu")
        print("2. Tìm kiếm món")
        print("3. Đặt món")
        print("4. Xem đơn hàng")
        print("5. Hủy đơn")
        print("0. Thoát")
        c = input("Chọn: ")

        if c == "1":
            show_menu()
        elif c == "2":
            kw = input("Từ khóa: ")
            search_food(kw)
        elif c == "3":
            order_food(customer)
        elif c == "4":
            print("\n=== ĐƠN ĐÃ ĐẶT ===")
            for o in orders:
                if o["customer"] == customer.name:
                    print(o)
        elif c == "5":
            name = customer.name
            for o in orders:
                if o["customer"] == name and o["status"] == "Mới đặt":
                    orders.remove(o)
                    print("✅ Đã hủy đơn thành công.")
                    break
            else:
                print("❌ Không có đơn nào để hủy.")
        else:
            break
