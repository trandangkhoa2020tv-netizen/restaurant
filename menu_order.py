# menu_order.py

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

orders = []


def show_menu():
    print("\n========== DANH SÁCH MÓN ĂN ==========")
    for cat, items in menu_data.items():
        print(f"\n--- {cat.upper()} ---")
        print(f"{'Mã':<6} {'Tên món':<35} {'Khẩu vị':<25} {'Giá':<10} {'Tình trạng':<10}")
        for m in items:
            print(f"{m[0]:<6} {m[1]:<35} {m[2]:<25} {m[3]:<10,} {m[4]:<10}")
    print("--------------------------------------")


def search_food(keyword):
    print(f"\n🔍 Kết quả tìm kiếm cho '{keyword}':")
    found = False
    for cat, items in menu_data.items():
        for m in items:
            if keyword.lower() in m[1].lower():
                print(f"{m[0]} - {m[1]} ({m[3]:,}đ)")
                found = True
    if not found:
        print("❌ Không tìm thấy món phù hợp.")


def order_food(customer):
    show_menu()
    code = input("Nhập mã món muốn đặt: ").upper()
    quantity = int(input("Số lượng: "))
    note = input("Ghi chú (ví dụ: ít cay, không hành,...): ")
    delivery = input("Hình thức (tại chỗ/mang đi/giao hàng): ")

    for cat, items in menu_data.items():
        for m in items:
            if m[0] == code:
                total = m[3] * quantity
                order = {
                    "customer": customer.name,
                    "food": m[1],
                    "quantity": quantity,
                    "note": note,
                    "method": delivery,
                    "total": total,
                    "status": "Mới đặt"
                }
                orders.append(order)
                print(f"✅ Đặt món '{m[1]}' thành công! Tổng: {total:,}đ")
                return
    print("❌ Mã món không hợp lệ.")
