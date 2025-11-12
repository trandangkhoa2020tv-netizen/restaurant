# admin.py
from menu_order import menu_data

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Xem danh sách món")
        print("2. Thêm món")
        print("3. Xóa món")
        print("0. Thoát")
        c = input("Chọn: ")

        if c == "1":
            for cat, items in menu_data.items():
                print(f"\n--- {cat} ---")
                for m in items:
                    print(m)
        elif c == "2":
            cat = input("Loại món (Lẩu/Món khô/Nước uống): ")
            code = input("Mã món: ").upper()
            name = input("Tên món: ")
            flavor = input("Khẩu vị: ")
            price = int(input("Giá bán: "))
            menu_data[cat].append((code, name, flavor, price, "Còn", 0))
            print("Đã thêm món mới!")
        elif c == "3":
            code = input("Nhập mã món cần xóa: ").upper()
            for cat, items in menu_data.items():
                for m in items:
                    if m[0] == code:
                        items.remove(m)
                        print("Đã xóa món!")
                        break
        else:
            break
