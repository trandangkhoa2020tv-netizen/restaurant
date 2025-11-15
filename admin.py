from menu_order import menu_data
from auth import users, Customer, Staff, Admin

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Xem danh sách món")
        print("2. Thêm món")
        print("3. Xóa món")
        print("4. Quản lý nhân viên")
        print("5. Quản lý tài khoản")
        print("6. Quản lý hệ thống")
        print("0. Thoát")
        c = input("Chọn(0-6): ")

        if c == "1":
            show_menu()
        elif c == "2":
            add_food()
        elif c == "3":
            delete_food()
        elif c == "4":
            manage_staff()
        elif c == "5":
            manage_accounts()
        elif c == "6":
            system_settings()
        elif c == "0":
            break
        else:
            print("Lựa chọn không hợp lệ!")


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


# ===============================
# 4. Quản lý nhân viên
# ===============================
def manage_staff():
    print("\n=== QUẢN LÝ NHÂN VIÊN ===")
    staff_list = [u for u in users if u.role == "staff"]
    if not staff_list:
        print("Chưa có nhân viên nào.")
        return

    print("Danh sách nhân viên:")
    for i, s in enumerate(staff_list, 1):
        print(f"{i}. {s.name} | {s.phone} | {s.email}")


# ===============================
# 5. Quản lý tài khoản (User/Staff)
# ===============================
def manage_accounts():
    while True:
        print("\n=== QUẢN LÝ TÀI KHOẢN ===")
        print("1. Xem danh sách tất cả tài khoản")
        print("2. Xóa tài khoản")
        print("3. Thay đổi vai trò tài khoản")
        print("0. Quay lại")
        choice = input("Chọn(0-3): ")

        if choice == "1":
            if not users:
                print("Chưa có tài khoản nào.")
                continue
            print("\nDanh sách tài khoản:")
            for i, u in enumerate(users, 1):
                print(f"{i}. {u.name} | {u.phone} | {u.email} | Role: {u.role}")

        elif choice == "2":
            email = input("Nhập email tài khoản cần xóa: ")
            for u in users:
                if u.email == email:
                    users.remove(u)
                    print(f"Đã xóa tài khoản {email}.")
                    break
            else:
                print("Không tìm thấy tài khoản.")

        elif choice == "3":
            email = input("Nhập email tài khoản cần thay đổi vai trò: ")
            for u in users:
                if u.email == email:
                    print(f"Vai trò hiện tại: {u.role}")
                    print("Chọn vai trò mới:")
                    print("1. customer")
                    print("2. staff")
                    print("3. admin")
                    r = input("Chọn(1-3): ")
                    roles = {"1": "customer", "2": "staff", "3": "admin"}
                    if r in roles:
                        u.role = roles[r]
                        print(f"Đã cập nhật vai trò {u.name} → {u.role}")
                    else:
                        print("Vai trò không hợp lệ.")
                    break
            else:
                print("Không tìm thấy tài khoản.")

        elif choice == "0":
            break

        else:
            print("Lựa chọn không hợp lệ!")


# ===============================
# 6. Cài đặt hệ thống
# ===============================
def system_settings():
    print("\n=== CÀI ĐẶT HỆ THỐNG ===")
    print("1. Sao lưu dữ liệu")
    print("2. Khôi phục dữ liệu")
    print("0. Quay lại")

    input("Tính năng hệ thống đang phát triển. Nhấn Enter để quay lại.")
