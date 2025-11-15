# customer.py
from menu_order import orders, show_menu, search_food, menu_data

def customer_menu(customer):
    cart = []  # Giỏ hàng tạm thời

    while True:
        print("\n=== MENU KHÁCH HÀNG ===")
        print("1. Xem menu")
        print("2. Tìm kiếm món")
        print("3. Thêm món vào giỏ hàng")
        print("4. Xem giỏ hàng")
        print("5. Đặt món trong giỏ hàng")
        print("6. Xem đơn hàng")
        print("7. Hủy đơn")
        print("8. Cập nhật thông tin cá nhân")
        print("0. Thoát")
        c = input("Chọn(0-8): ")

        # --- HIỂN THỊ MENU MÓN ---
        if c == "1":
            show_menu()

        # --- TÌM KIẾM MÓN THEO TỪ KHÓA ---
        elif c == "2":
            kw = input("Từ khóa: ")
            search_food(kw)

        # --- THÊM MÓN VÀO GIỎ HÀNG ---
        elif c == "3":
            code = input("Nhập mã món muốn thêm vào giỏ: ").upper()
            quantity = int(input("Số lượng: "))
            note = input("Ghi chú: ")

            found = False
            for cat, items in menu_data.items():
                for m in items:
                    if m[0] == code:
                        cart.append({
                            "food": m[1],
                            "code": m[0],
                            "quantity": quantity,
                            "note": note,
                            "price": m[3]
                        })
                        print(f"Đã thêm {m[1]} x{quantity} vào giỏ hàng.")
                        found = True
                        break
                if found:
                    break
            if not found:
                print("Mã món không hợp lệ.")

        # --- XEM GIỎ HÀNG ---
        elif c == "4":
            if not cart:
                print("Giỏ hàng trống.")
            else:
                while True:
                    print("\n=== GIỎ HÀNG ===")
                    total_cart = 0
                    for i, item in enumerate(cart, start=1):
                        subtotal = item['quantity'] * item['price']
                        total_cart += subtotal
                        print(f"{i}. {item['food']} x{item['quantity']} - {subtotal:,}đ - Ghi chú: {item['note']}")
                    print(f"Tổng tiền trong giỏ: {total_cart:,}đ")
                    print("\nTùy chọn:")
                    print("1. Chỉnh số lượng món")
                    print("2. Xóa món")
                    print("0. Quay lại menu")
                    choice_cart = input("Chọn(0-2): ")

                    if choice_cart == "1":
                        try:
                            idx = int(input("Nhập số thứ tự món cần chỉnh số lượng: ")) - 1
                            if 0 <= idx < len(cart):
                                new_qty = int(input(f"Số lượng mới cho {cart[idx]['food']}: "))
                                if new_qty > 0:
                                    cart[idx]['quantity'] = new_qty
                                    print(f"Cập nhật số lượng {cart[idx]['food']} thành {new_qty}.")
                                else:
                                    print("Số lượng phải lớn hơn 0.")
                            else:
                                print("Số thứ tự không hợp lệ.")
                        except ValueError:
                            print("Vui lòng nhập số hợp lệ.")
                    elif choice_cart == "2":
                        try:
                            idx = int(input("Nhập số thứ tự món cần xóa: ")) - 1
                            if 0 <= idx < len(cart):
                                removed_item = cart.pop(idx)
                                print(f"Đã xóa {removed_item['food']} khỏi giỏ hàng.")
                            else:
                                print("Số thứ tự không hợp lệ.")
                        except ValueError:
                            print("Vui lòng nhập số hợp lệ.")
                    elif choice_cart == "0":
                        break
                    else:
                        print("Lựa chọn không hợp lệ, vui lòng thử lại.")


       # --- ĐẶT MÓN TỪ GIỎ HÀNG ---
        elif c == "5":
            if not cart:
                print("Giỏ hàng trống. Hãy thêm món trước khi đặt.")
                continue

            print("\nChọn hình thức đặt:")
            print("1. Đặt bàn (ăn tại nhà hàng)")
            print("2. Giao hàng tận nơi")
            print("3. Mang đi (tự đến lấy)")
            choice = input("Chọn(1-3): ")

            method = None
            selected_table = None

            if choice == "1":
                method = "đặt bàn"
                from menu_order import tables, show_tables
                print("\n===== CÁC BÀN CÒN TRỐNG =====")
                show_tables(only_empty=True)
                try:
                    table_id = int(input("Chọn số bàn (1-10): "))
                    if table_id in tables and tables[table_id] == "Trống":
                        tables[table_id] = f"Đã đặt bởi {customer.name}"
                        selected_table = table_id
                        print(f"Bàn {table_id} đã được đặt thành công!")
                    else:
                        print("Bàn không hợp lệ hoặc đã có người đặt.")
                        continue
                except ValueError:
                    print("Vui lòng nhập số bàn hợp lệ (1-10).")
                    continue
            elif choice == "2":
                method = "giao hàng"
            elif choice == "3":
                method = "mang đi"
            else:
                print("Lựa chọn không hợp lệ.")
                continue

            # Chọn hình thức thanh toán
            print("\nChọn hình thức thanh toán:")
            print("1. Tiền mặt")
            print("2. Chuyển khoản")
            payment_choice = input("Chọn(1-2): ")
            if payment_choice == "1":
                payment_method = "Tiền mặt"
            elif payment_choice == "2":
                payment_method = "Chuyển khoản"
            else:
                print("Lựa chọn thanh toán không hợp lệ. Đơn hàng chưa được đặt.")
                continue

            # Thêm tất cả món trong giỏ vào orders
            for item in cart:
                total = item['quantity'] * item['price']
                order = {
                    "customer": customer.name,
                    "food": item['food'],
                    "quantity": item['quantity'],
                    "note": item['note'],
                    "method": method,
                    "payment": payment_method,
                    "table": selected_table if selected_table else "-",
                    "total": total,
                    "status": "Mới đặt",
                    "email": customer.email,
                    "dob": customer.dob,
                    "gender": customer.gender,
                    "address": customer.address,
                    "phone": customer.phone
                }
                orders.append(order)

            print("Đã đặt thành công các món trong giỏ hàng!")
            print(f"Hình thức thanh toán: {payment_method}")
            cart.clear()  # Xóa giỏ sau khi đặt

        # --- XEM CÁC ĐƠN ĐÃ ĐẶT ---
        elif c == "6":
            print("\n=== ĐƠN ĐÃ ĐẶT ===")
            has_order = False
            for o in orders:
                if o.get("email") == getattr(customer, "email", ""):
                    has_order = True
                    print(f"Khách hàng: {o.get('customer','')}")
                    print(f"Địa chỉ: {o.get('address','')}")
                    print(f"Số điện thoại: {o.get('phone','')}")
                    print(f"Món: {o.get('food','')} x{o.get('quantity','')}")
                    print(f"Ghi chú: {o.get('note','')}")
                    print(f"Hình thức: {o.get('method','')}")
                    print(f"Tổng tiền: {o.get('total',0):,}đ")
                    print(f"Trạng thái: {o.get('status','')}")
                    print("-"*40)
            if not has_order:
                print("Chưa có đơn hàng nào.")

        # --- HỦY ĐƠN ---
        elif c == "7":
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
        elif c == "8":
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
