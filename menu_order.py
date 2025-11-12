# menu_order.py
menu = {
    "lau": [
        {"id": "L001", "name": "Lẩu Thái hải sản chua cay", "flavor": "Chua cay, đậm đà", "price": 289000, "status": "Còn", "orders": 152},
        {"id": "L002", "name": "Lẩu bò nhúng giấm", "flavor": "Chua nhẹ, thơm giấm, ngọt thịt", "price": 269000, "status": "Còn", "orders": 134},
        {"id": "L003", "name": "Lẩu nấm chay thanh đạm", "flavor": "Ngọt tự nhiên, thanh mát", "price": 239000, "status": "Còn", "orders": 78},
        {"id": "L004", "name": "Lẩu kim chi Hàn Quốc", "flavor": "Cay nồng, vị đậm", "price": 259000, "status": "Còn", "orders": 201},
    ],
    "kho": [
        {"id": "K001", "name": "Cánh gà chiên nước mắm", "flavor": "Mặn ngọt, giòn tan", "price": 89000, "status": "Còn", "orders": 243},
        {"id": "K002", "name": "Bò lúc lắc khoai tây chiên", "flavor": "Đậm vị, béo nhẹ", "price": 119000, "status": "Còn", "orders": 175},
        {"id": "K003", "name": "Cá hồi áp chảo sốt bơ tỏi", "flavor": "Béo ngậy, thơm bơ", "price": 139000, "status": "Còn", "orders": 92},
        {"id": "K004", "name": "Tôm rim me", "flavor": "Chua ngọt, đậm đà", "price": 109000, "status": "Còn", "orders": 84},
        {"id": "K005", "name": "Mực nướng sa tế", "flavor": "Cay thơm, giòn nhẹ", "price": 115000, "status": "Còn", "orders": 148},
        {"id": "K006", "name": "Sườn non rim mặn ngọt", "flavor": "Đậm vị, mềm thơm", "price": 99000, "status": "Còn", "orders": 121},
        {"id": "K007", "name": "Cơm chiên hải sản", "flavor": "Thơm, vừa vị", "price": 79000, "status": "Còn", "orders": 187},
        {"id": "K008", "name": "Gỏi bò bóp thấu", "flavor": "Chua ngọt, cay nhẹ", "price": 85000, "status": "Còn", "orders": 133},
    ],
    "drink": [
        {"id": "D001", "name": "Coca-Cola", "flavor": "Ngọt, có gas", "price": 25000, "status": "Còn", "orders": 312},
        {"id": "D002", "name": "Pepsi", "flavor": "Ngọt, có gas", "price": 25000, "status": "Còn", "orders": 289},
        {"id": "D003", "name": "7Up", "flavor": "Ngọt nhẹ, thanh mát", "price": 25000, "status": "Còn", "orders": 214},
        {"id": "D004", "name": "Trà đào cam sả", "flavor": "Ngọt thanh, thơm mùi sả", "price": 39000, "status": "Còn", "orders": 185},
        {"id": "D005", "name": "Nước suối Aquafina", "flavor": "Nhẹ, không gas", "price": 15000, "status": "Còn", "orders": 267},
    ]
}

orders = []

def show_menu():
    print("\n==================== MENU NHÀ HÀNG ====================")
    sections = {
        "lau": "🍲 MÓN LẨU",
        "kho": "🍗 MÓN KHÔ",
        "drink": "🥤 NƯỚC UỐNG"
    }

    for key, title in sections.items():
        print(f"\n--- {title} ---")
        print("{:<6} {:<35} {:<25} {:<10} {:<8} {:<10}".format(
            "Mã", "Tên món", "Khẩu vị", "Giá", "TT", "Lượt đặt"
        ))
        print("-" * 100)
        for m in menu[key]:
            print("{:<6} {:<35} {:<25} {:<10,.0f} {:<8} {:<10}".format(
                m["id"], m["name"], m["flavor"], m["price"], m["status"], m["orders"]
            ))

def order_food(customer):
    cart = []
    while True:
        show_menu()
        choice = input("\nNhập MÃ MÓN muốn thêm (hoặc 0 để đặt hàng): ").upper()
        if choice == "0":
            break

        found = None
        for category in menu.values():
            for m in category:
                if m["id"] == choice:
                    found = m
                    break

        if found:
            quantity = int(input("Số lượng: "))
            note = input("Ghi chú (ví dụ: ít cay, không hành...): ")
            cart.append({"item": found, "qty": quantity, "note": note})
            print(f"✅ Đã thêm {found['name']} vào giỏ hàng!")
        else:
            print("❌ Không tìm thấy mã món này, vui lòng thử lại.")

    if cart:
        orders.append({
            "customer": customer.name,
            "items": cart,
            "status": "Mới đặt"
        })
        print("\n🧾 Đơn hàng của bạn đã được tạo thành công!")
    else:
        print("❌ Chưa chọn món nào!")
