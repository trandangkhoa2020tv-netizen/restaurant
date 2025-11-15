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
        print("6. Cập nhật thông tin cá nhân")
        print("0. Thoát")
        c = input("Chọn: ")

        # --- HIỂN THỊ MENU MÓN ---
        if c == "1":
            show_menu()

        # --- TÌM KIẾM MÓN THEO TỪ KHÓA ---
        elif c == "2":
            kw = input("Từ khóa: ")
            search_food(kw)

        # --- ĐẶT MÓN ---
        elif c == "3":
            order_food(customer)

        # --- XEM CÁC ĐƠN ĐÃ ĐẶT ---
        elif c == "4":
            print("\n=== ĐƠN ĐÃ ĐẶT ===")
            has_order = False
            for o in orders:
                # So sánh bằng email để tránh trùng tên
                if o.get("email") == getattr(customer, "email", ""):
                    has_order = True
                    print(f"Khách hàng: {o.get('customer','')}")
                    print(f"Ngày sinh: {o.get('dob','')}")
                    print(f"Giới tính: {o.get('gender','')}")
                    print(f"Địa chỉ: {o.get('address','')}")
                    print(f"Số điện thoại: {o.get('phone','')}")
                    print(f"Món: {o.get('item','')}")
                    print(f"Số lượng: {o.get('quantity','')}")
                    print(f"Ghi chú: {o.get('note','')}")
                    print(f"Hình thức: {o.get('method','')}")
                    print(f"Tổng tiền: {o.get('total',0):,}đ")
                    print(f"Trạng thái: {o.get('status','')}")
                    print("-"*40)
            if not has_order:
                print("Chưa có đơn hàng nào.")

        # --- HỦY ĐƠN ---
        elif c == "5":
            found = False
            for o in orders:
                if o.get("email") == getattr(customer, "email", "") and o.get("status") == "Mới đặt":
                    orders.remove(o)
                    print("Đã hủy đơn thành công.")
                    found = True
                    break
            if not found:
                print("Không có đơn nào để hủy.")

        # --- CẬP NHẬT THÔNG TIN CÁ NHÂN ---
        elif c == "6":
            print("\n=== CẬP NHẬT THÔNG TIN CÁ NHÂN ===")
            customer.name = input(f"Họ tên ({customer.name}): ") or customer.name
            customer.dob = input(f"Ngày sinh ({getattr(customer,'dob','')}): ") or getattr(customer,'dob','')
            customer.gender = input(f"Giới tính ({getattr(customer,'gender','')}): ") or getattr(customer,'gender','')
            customer.address = input(f"Địa chỉ ({getattr(customer,'address','')}): ") or getattr(customer,'address','')
            customer.phone = input(f"Số điện thoại ({customer.phone}): ") or customer.phone
            customer.password = input("Mật khẩu (giữ nguyên nếu không đổi): ") or customer.password
            print("Cập nhật thông tin thành công!")

        # --- THOÁT MENU ---
        elif c == "0":
            break

        else:
            print("Lựa chọn không hợp lệ, vui lòng chọn lại.")
