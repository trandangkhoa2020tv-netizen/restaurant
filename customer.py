# customer.py
# Import các hàm liên quan đến đặt món, danh sách đơn hàng, hiển thị menu và tìm kiếm món
from menu_order import order_food, orders, show_menu, search_food

def customer_menu(customer):
    # customer: là object Customer đã đăng nhập

    while True:
        # ----- MENU KHÁCH HÀNG -----
        print("\n=== MENU KHÁCH HÀNG ===")
        print("1. Xem menu")
        print("2. Tìm kiếm món")
        print("3. Đặt món")
        print("4. Xem đơn hàng")
        print("5. Hủy đơn")
        print("0. Thoát")
        c = input("Chọn: ")

        # --- HIỂN THỊ MENU MÓN ---
        if c == "1":
            show_menu()

        # --- TÌM KIẾM MÓN THEO TỪ KHÓA ---
        elif c == "2":
            kw = input("Từ khóa: ")
            search_food(kw)

        # --- ĐẶT MÓN (tạo đơn hàng mới) ---
        elif c == "3":
            # Gọi hàm order_food và truyền vào customer hiện tại
            order_food(customer)

        # --- XEM CÁC ĐƠN ĐÃ ĐẶT CỦA KHÁCH HÀNG ---
        elif c == "4":
            print("\n=== ĐƠN ĐÃ ĐẶT ===")
            # Mỗi đơn hàng o là 1 dict: {"customer": ..., "item": ..., "status": ...}
            for o in orders:
                if o["customer"] == customer.name:
                    print(o)

        # --- HỦY ĐƠN (chỉ hủy đơn đang ở trạng thái "Mới đặt") ---
        elif c == "5":
            name = customer.name
            found = False
            for o in orders:
                # Chỉ hủy đơn của chính khách hàng và chưa chế biến
                if o["customer"] == name and o["status"] == "Mới đặt":
                    orders.remove(o)
                    print("Đã hủy đơn thành công.")
                    found = True
                    break

            if not found:
                print("Không có đơn nào để hủy.")

        # --- THOÁT MENU ---
        else:
            break
