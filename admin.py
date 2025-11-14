# admin.py
from menu_order import menu_data   # Import dữ liệu menu (dict chứa danh sách món)

def admin_menu():
    while True:
        # Menu dành cho admin
        print("\n=== MENU ADMIN ===")
        print("1. Xem danh sách món")
        print("2. Thêm món")
        print("3. Xóa món")
        print("0. Thoát")
        c = input("Chọn: ")

        # --- XEM DANH SÁCH MÓN ---
        if c == "1":
            # menu_data: {"Lẩu": [...], "Món khô": [...], "Nước uống": [...]}
            for cat, items in menu_data.items():
                print(f"\n--- {cat} ---")  # In tên loại món
                for m in items:            # m = (code, name, flavor, price, status, orders)
                    print(m)

        # --- THÊM MÓN MỚI ---
        elif c == "2":
            # Nhập thông tin món ăn
            cat = input("Loại món (Lẩu/Món khô/Nước uống): ")
            code = input("Mã món: ").upper()
            name = input("Tên món: ")
            flavor = input("Khẩu vị: ")
            price = int(input("Giá bán: "))

            # Thêm vào danh sách: (mã, tên, khẩu vị, giá, tình trạng, lượt đặt)
            menu_data[cat].append((code, name, flavor, price, "Còn", 0))
            print("Đã thêm món mới!")

        # --- XÓA MÓN THEO MÃ ---
        elif c == "3":
            code = input("Nhập mã món cần xóa: ").upper()

            # Duyệt tất cả category để tìm món
            for cat, items in menu_data.items():
                for m in items:
                    if m[0] == code:    # m[0] = mã món
                        items.remove(m)
                        print("Đã xóa món!")
                        break

        # --- THOÁT MENU ADMIN ---
        else:
            break
