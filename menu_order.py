# menu_order.py

# ===========================
# DỮ LIỆU MENU MÓN ĂN MẶC ĐỊNH
# ===========================
# menu_data là dictionary, mỗi key là 1 loại món
# value là 1 list gồm các tuple: (mã món, tên món, khẩu vị, giá, tình trạng, số lượt đặt)
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

# Danh sách đơn hàng (mỗi đơn là 1 dictionary)
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

        # mỗi m là 1 tuple món
        for m in items:
            print(f"{m[0]:<6} {m[1]:<35} {m[2]:<25} {m[3]:<10,} {m[4]:<10}")
    print("--------------------------------------")


# ===========================
# TÌM KIẾM MÓN ĂN
# ===========================
def search_food(keyword):
    print(f"\nKết quả tìm kiếm cho '{keyword}':")
    found = False

    # duyệt qua tất cả món
    for cat, items in menu_data.items():
        for m in items:
            # So sánh từ khóa với tên món (không phân biệt hoa thường)
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
        # only_empty=True → chỉ in bàn Trống
        if only_empty and status != "Trống":
            continue
        print(f"Bàn {t}: {status}")
    print("--------------------------")


# ===========================
# ĐẶT MÓN
# ===========================
def order_food(customer):
    # 1. Hiển thị menu trước để khách chọn
    show_menu()

    # 2. Nhập mã món + số lượng + ghi chú
    code = input("Nhập mã món muốn đặt: ").upper()
    quantity = int(input("Số lượng: "))
    note = input("Ghi chú (ví dụ: ít cay, không hành,...): ")

    # 3. Chọn hình thức đặt món
    print("\nChọn hình thức đặt:")
    print("1. Đặt bàn (ăn tại nhà hàng)")
    print("2. Giao hàng tận nơi")
    print("3. Mang đi (tự đến lấy)")
    choice = input("Nhập lựa chọn (1-3): ")

    method = None
    selected_table = None

    # ---------------------------
    # TRƯỜNG HỢP 1: ĐẶT BÀN
    # ---------------------------
    if choice == "1":
        method = "đặt bàn"

        # Hiển thị danh sách bàn trống
        print("\n===== CÁC BÀN CÒN TRỐNG =====")
        show_tables(only_empty=True)

        try:
            table_id = int(input("Chọn số bàn (1-10): "))

            if table_id in tables:
                # Nếu bàn đang trống → cho đặt
                if tables[table_id] == "Trống":
                    tables[table_id] = f"Đã đặt bởi {customer.name}"
                    selected_table = table_id
                    print(f"Bàn {table_id} đã được đặt thành công!")
                else:
                    print("Bàn này đã có người đặt, vui lòng chọn bàn khác.")
                    return
            else:
                print("Số bàn không hợp lệ.")
                return
        except ValueError:
            print("Vui lòng nhập số bàn hợp lệ (1-10).")
            return

    # ---------------------------
    # TRƯỜNG HỢP 2: GIAO HÀNG
    # ---------------------------
    elif choice == "2":
        method = "giao hàng"

    # ---------------------------
    # TRƯỜNG HỢP 3: MANG ĐI
    # ---------------------------
    elif choice == "3":
        method = "mang đi"

    else:
        print("Lựa chọn không hợp lệ.")
        return

    # ================================
    # TÌM MÓN TRONG MENU THEO MÃ CODE
    # ================================
    for cat, items in menu_data.items():
        for m in items:
            if m[0] == code:
                total = m[3] * quantity

                # Tạo dictionary đơn hàng
                order = {
                    "customer": customer.name,
                    "food": m[1],
                    "quantity": quantity,
                    "note": note,
                    "method": method,
                    "table": selected_table if selected_table else "-",
                    "total": total,
                    "status": "Mới đặt"
                }

                # Lưu vào danh sách orders
                orders.append(order)

                print(f"Đặt món '{m[1]}' thành công! Tổng: {total:,}đ")
                if method == "đặt bàn":
                    print(f"Bàn: {selected_table}")
                return

    # Nếu không tìm thấy mã món
    print("Mã món không hợp lệ.")
