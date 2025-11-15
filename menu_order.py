# menu_order.py

# ===========================
# DỮ LIỆU MENU MÓN ĂN MẶC ĐỊNH
# ===========================
menu_data = {
    "Lẩu": [
        ("L001", "Lẩu Thái hải sản chua cay", "Chua cay, đậm đà", 289000, "Còn", 152),
        ("L002", "Lẩu bò nhúng giấm", "Chua nhẹ, thơm giấm, ngọt thịt", 269000, "Còn", 134),
        ("L003", "Lẩu nấm chay thanh đạm", "Ngọt tự nhiên, thanh mát", 239000, "Còn", 78),
        ("L004", "Lẩu kim chi Hàn Quốc", "Cay nồng, vị đậm", 259000, "Còn", 201),
    ],
    "Món khô": [
        ("K001", "Cánh gà chiên nước mắm", "Mặn ngọt, giòn tan", 89000, "Còn", 243),
        ("K002", "Bò lúc lắc khoai tây chiên", "Đậm vị, béo nhẹ", 119000, "Còn", 175),
        ("K003", "Cá hồi áp chảo sốt bơ tỏi", "Béo ngậy, thơm bơ", 139000, "Còn", 92),
        ("K004", "Tôm rim me", "Chua ngọt, đậm đà", 109000, "Còn", 84),
        ("K005", "Mực nướng sa tế", "Cay thơm, giòn nhẹ", 115000, "Còn", 148),
        ("K006", "Sườn non rim mặn ngọt", "Đậm vị, mềm thơm", 99000, "Còn", 121),
        ("K007", "Cơm chiên hải sản", "Thơm, vừa vị", 79000, "Còn", 187),
        ("K008", "Gỏi bò bóp thấu", "Chua ngọt, cay nhẹ", 85000, "Còn", 133),
    ],
    "Nước uống": [
        ("D001", "Coca-Cola", "Ngọt, có gas", 25000, "Còn", 312),
        ("D002", "Pepsi", "Ngọt, có gas", 25000, "Còn", 289),
        ("D003", "7Up", "Ngọt nhẹ, thanh mát", 25000, "Còn", 214),
        ("D004", "Trà đào cam sả", "Ngọt thanh, thơm mùi sả", 39000, "Còn", 185),
        ("D005", "Nước suối Aquafina", "Nhẹ, không gas", 15000, "Còn", 267),
    ]
}

# Danh sách đơn hàng
orders = []

# Tạo 10 bàn, mặc định tất cả đều "Trống"
tables = {i: "Trống" for i in range(1, 11)}

# ===========================
# HIỂN THỊ MENU
# ===========================
def show_menu():
    print("\n========== DANH SÁCH MÓN ĂN ==========")
    for cat, items in menu_data.items():
        print(f"\n--- {cat.upper()} ---")
        print(f"{'Mã':<6} {'Tên món':<35} {'Khẩu vị':<25} {'Giá':<10} {'Tình trạng':<10}")
        for m in items:
            print(f"{m[0]:<6} {m[1]:<35} {m[2]:<25} {m[3]:<10,} {m[4]:<10}")
    print("--------------------------------------")

# ===========================
# TÌM KIẾM MÓN ĂN
# ===========================
def search_food(keyword):
    print(f"\nKết quả tìm kiếm cho '{keyword}':")
    found = False
    for cat, items in menu_data.items():
        for m in items:
            if keyword.lower() in m[1].lower():
                print(f"{m[0]} - {m[1]} ({m[3]:,}đ)")
                found = True
    if not found:
        print("Không tìm thấy món phù hợp.")

# ===========================
# HIỂN THỊ DANH SÁCH BÀN
# ===========================
def show_tables(only_empty=False):
    print("\n===== DANH SÁCH BÀN =====")
    for t, status in tables.items():
        if only_empty and status != "Trống":
            continue
        print(f"Bàn {t}: {status}")
    print("--------------------------")

# ===========================
# ĐẶT MÓN
# ===========================
def order_food(customer):
    show_menu()
    code = input("Nhập mã món muốn đặt: ").upper()
    quantity = int(input("Số lượng: "))
    note = input("Ghi chú (ví dụ: ít cay, không hành,...): ")

    print("\nChọn hình thức đặt:")
    print("1. Đặt bàn (ăn tại nhà hàng)")
    print("2. Giao hàng tận nơi")
    print("3. Mang đi (tự đến lấy)")
    choice = input("Chọn: ")

    method = None
    selected_table = None

    # Đặt bàn
    if choice == "1":
        method = "đặt bàn"
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
                return
        except ValueError:
            print("Vui lòng nhập số bàn hợp lệ (1-10).")
            return
    # Giao hàng
    elif choice == "2":
        method = "giao hàng"
    # Mang đi
    elif choice == "3":
        method = "mang đi"
    else:
        print("Lựa chọn không hợp lệ.")
        return

    # Tìm món
    for cat, items in menu_data.items():
        for m in items:
            if m[0] == code:
                total = m[3] * quantity
                order = {
                    "customer": customer.name,
                    "email": getattr(customer, "email", ""),
                    "dob": getattr(customer, "dob", ""),
                    "gender": getattr(customer, "gender", ""),
                    "address": getattr(customer, "address", ""),
                    "phone": getattr(customer, "phone", ""),
                    "item": m[1],
                    "quantity": quantity,
                    "note": note,
                    "method": method,
                    "table": selected_table if selected_table else "-",
                    "total": total,
                    "status": "Mới đặt"
                }
                orders.append(order)
                print(f"Đặt món '{m[1]}' thành công! Tổng: {total:,}đ")
                if method == "đặt bàn":
                    print(f"Bàn: {selected_table}")
                return

    print("Mã món không hợp lệ.")
