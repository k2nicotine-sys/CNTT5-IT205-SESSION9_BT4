order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng")
    print("4. Thoát")
    choice = input("Nhập lựa chọn: ").strip()
    match choice:
        case "1":
            if len(order_list) == 0:
                print("Danh sách đơn hàng hiện đang trống.")
            else:
                for index, order in enumerate(order_list, start=1):
                    print(f"{index}. {order}")

        case "2":
            print("1. Thêm đơn hàng")
            print("2. Sửa đơn hàng")
            print("3. Xóa đơn hàng")
            print("4. Quay lại")
            update_choice = input("Nhập lựa chọn: ").strip()
            match update_choice:
                case "1":
                    code = input("Nhập mã đơn hàng: ").strip().upper()
                    status = input("Nhập trạng thái: ").strip().upper()
                    order_list.append(f"{code} - {status}")
                    print("Thêm thành công!")
                case "2":
                    position = input("Nhập vị trí cần sửa: ").strip()
                    if position.isdigit():
                        index = int(position) - 1
                        if 0 <= index < len(order_list):
                            code = input("Nhập mã mới: ").strip().upper()
                            status = input("Nhập trạng thái mới: ").strip().upper()

                            order_list[index] = f"{code} - {status}"

                            print("Cập nhật thành công!")
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")
                    else:
                        print("Vị trí không hợp lệ!")

                case "3":
                    position = input("Nhập vị trí cần xóa: ").strip()

                    if position.isdigit():
                        index = int(position) - 1

                        if 0 <= index < len(order_list):
                            removed_order = order_list.pop(index)

                            print("Đã xóa:", removed_order)
                        else:
                            print("Không tồn tại đơn hàng ở vị trí này!")
                    else:
                        print("Vị trí không hợp lệ!")

                case "4":
                    continue
                case _:
                    print("Lựa chọn không hợp lệ!")

        case "3":
            pending = 0
            delivering = 0
            completed = 0
            cancelled = 0
            for order in order_list:
                status = order.split(" - ")[1]

                match status:
                    case "PENDING":
                        pending += 1
                    case "DELIVERING":
                        delivering += 1
                    case "COMPLETED":
                        completed += 1
                    case "CANCELLED":
                        cancelled += 1
                        
            print("PENDING:", pending)
            print("DELIVERING:", delivering)
            print("COMPLETED:", completed)
            print("CANCELLED:", cancelled)
            print("Tổng:", len(order_list))

        case "4":
            print("Thoát chương trình.")
            break

        case _:
            print("Lựa chọn không hợp lệ!")