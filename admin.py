from menu_order import menu

def admin_menu():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Xem danh sách món")
        print("2. Thêm món")
        print("3. Xóa món")
        print("0. Thoát")
        c = input("Chọn: ")
        if c == "1":
            for m in menu:
                print(m)
        elif c == "2":
            name = input("Tên món: ")
            price = int(input("Giá: "))
            category = input("Loại (main/drink/other): ")
            menu.append({"id": len(menu)+1, "name": name, "price": price, "category": category})
            print("Đã thêm món!")
        elif c == "3":
            id_rm = int(input("Nhập ID món muốn xóa: "))
            for m in menu:
                if m["id"] == id_rm:
                    menu.remove(m)
                    print("Đã xóa!")
                    break
        else:
            break
