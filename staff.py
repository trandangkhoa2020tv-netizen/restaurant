from menu_order import orders, tables
from menu_order import menu_data

def staff_menu(user):
    while True:
        print("\n=== MENU NHÂN VIÊN ===")
        print("1. Xem tất cả đơn hàng")
        print("2. Cập nhật trạng thái đơn")
        print("3. Quản lý bàn (xem/cập nhật)")
        print("4. Xem danh sách món")
        print("5. Thêm món")
        print("6. Xóa món")
        print("0. Thoát")
        c = input("Chọn(0-6): ")

        if c == "1":
            view_orders()
        elif c == "2":
            update_order_status()
        elif c == "3":
            manage_tables()
        elif c == "4":
            show_menu()
        elif c == "5":
            add_food()
        elif c == "6":
            delete_food()
        elif c == "0":
            
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng nhập lại.")


# ===============================
# 1. Xem danh sách món
# ===============================
def show_menu():
    print("\n=== DANH SÁCH MÓN ===")
    for cat, items in menu_data.items():
        print(f"\n--- {cat} ---")
        for m in items:
            print(m)


# ===============================
# 2. Thêm món
# ===============================
def add_food():
    print("\nChọn loại món:")
    print("1. Lẩu")
    print("2. Món khô")
    print("3. Nước uống")

    choice = input("Chọn(1-3): ")
    categories = {"1": "Lẩu", "2": "Món khô", "3": "Nước uống"}

    if choice not in categories:
        print("Loại món không hợp lệ!")
        return

    cat = categories[choice]
    code = input("Mã món: ").upper()
    name = input("Tên món: ")
    flavor = input("Khẩu vị: ")
    price = int(input("Giá bán: "))

    menu_data[cat].append((code, name, flavor, price, "Còn", 0))
    print("Đã thêm món mới!")


# ===============================
# 3. Xóa món
# ===============================
def delete_food():
    code = input("Nhập mã món cần xóa: ").upper()

    for cat, items in menu_data.items():
        for m in items:
            if m[0] == code:
                items.remove(m)
                print("Đã xóa món!")
                return

    print("Không tìm thấy mã món!")


# 🔹 XEM TẤT CẢ ĐƠN HÀNG
def view_orders():
    if not orders:
        print("Chưa có đơn hàng nào.")
        return

    print("\n=== DANH SÁCH ĐƠN HÀNG ===")
    for i, o in enumerate(orders, start=1):
        print(f"\nĐơn #{i}:")
        print(f"👤 Khách hàng: {o['customer']}")
        print(f"🍽 Món: {o['item']} x {o['quantity']}")
        print(f"Ghi chú: {o['note']}")
        print(f"Hình thức: {o['method']}")
        if o["table"] != "-":
            print(f"Bàn: {o['table']}")
        print(f"Tổng tiền: {o['total']:,}đ")
        print(f"Trạng thái: {o['status']}")
        print("-" * 40)


# 🔹 CẬP NHẬT TRẠNG THÁI ĐƠN HÀNG
def update_order_status():
    if not orders:
        print("Không có đơn nào để cập nhật.")
        return

    try:
        order_index = int(input("Nhập số thứ tự đơn cần cập nhật: ")) - 1

        if 0 <= order_index < len(orders):
            print("\n=== CHỌN TRẠNG THÁI MỚI ===")
            print("1. Xác nhận")
            print("2. Chế biến")
            print("3. Hoàn tất")
            print("4. Hủy")
            opt = input("Chọn(1-4): ")

            status_map = {
                "1": "xác nhận",
                "2": "chế biến",
                "3": "hoàn tất",
                "4": "hủy"
            }

            if opt not in status_map:
                print("Lựa chọn không hợp lệ.")
                return

            new_status = status_map[opt]
            orders[order_index]["status"] = new_status
            print("Đã cập nhật trạng thái đơn hàng!")

            order = orders[order_index]

            # Giải phóng bàn khi hoàn tất hoặc hủy
            if order["table"] != "-" and new_status in ["hoàn tất", "hủy"]:
                table_id = order["table"]
                if table_id in tables:
                    tables[table_id] = "Trống"
                    print(f"🧹 Bàn {table_id} đã được dọn và chuyển về trạng thái trống.")

        else:
            print("Số thứ tự không hợp lệ.")

    except ValueError:
        print("Vui lòng nhập số hợp lệ.")


# 🔹 QUẢN LÝ BÀN
def manage_tables():
    while True:
        print("\n=== QUẢN LÝ BÀN ===")
        print("1. Xem danh sách bàn")
        print("2. Cập nhật trạng thái bàn")
        print("0. Quay lại")
        opt = input("Chọn(0-2): ")

        if opt == "1":
            show_tables()
        elif opt == "2":
            update_table_status()
        elif opt == "0":
            break
        else:
            print("Vui lòng chọn đúng số.")


# 🔹 HIỂN THỊ DANH SÁCH BÀN
def show_tables():
    print("\n===== DANH SÁCH BÀN =====")
    for t, status in tables.items():
        print(f"Bàn {t}: {status}")
    print("--------------------------")


# 🔹 CẬP NHẬT TRẠNG THÁI BÀN
def update_table_status():
    try:
        table_id = int(input("Nhập số bàn (1-10): "))

        if table_id in tables:
            print("\n=== TRẠNG THÁI BÀN ===")
            print("1. Trống")
            print("2. Đang phục vụ")
            print("3. Đã dọn")

            opt = input("Chọn(1-3): ")

            status_map = {
                "1": "Trống",
                "2": "Đang phục vụ",
                "3": "Đã dọn"
            }

            if opt not in status_map:
                print("Lựa chọn không hợp lệ.")
                return

            new_status = status_map[opt]
            tables[table_id] = new_status
            print(f"Đã cập nhật bàn {table_id} thành: {new_status}")

        else:
            print("Không tồn tại bàn này.")

    except ValueError:
        print("Nhập số bàn hợp lệ (1-10).")
