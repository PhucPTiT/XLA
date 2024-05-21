import cv2
import numpy as np

# Định nghĩa hàm kiểm tra va chạm giữa Dino và đối tượng khác (ví dụ: các xe trên đường)
def check_collision(dino, objects):
    dino_x1, dino_y1, dino_x2, dino_y2 = dino.get_position()

    for obj in objects:
        obj_x1, obj_y1, obj_x2, obj_y2 = obj.get_position()

        # Kiểm tra va chạm theo các chiều x và y
        if (
            dino_x2 >= obj_x1 and
            dino_x1 <= obj_x2 and
            dino_y2 >= obj_y1 and
            dino_y1 <= obj_y2
        ):
            return True

    return False

# Định nghĩa lớp đối tượng (ví dụ: xe trên đường)
class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_position(self):
        return self.x, self.y, self.x + self.width, self.y + self.height

# Đoạn mã dưới đây minh họa cách sử dụng các phần trên để điều khiển Dino và phát hiện va chạm.
if __name__ == "__main__":
    # Khởi tạo Dino và danh sách đối tượng (ví dụ: xe trên đường)
    dino = GameObject(100, 300, 50, 50)
    objects = [GameObject(200, 300, 30, 30), GameObject(300, 300, 40, 40)]

    # Vòng lặp chính
    while True:
        # Xử lý sự kiện nhảy (ví dụ: khi người chơi ấn space)
        key = cv2.waitKey(10)
        if key == ord(" "):
            if dino.y == 300:  # Kiểm tra xem Dino có ở mặt đất không
                dino.y -= 100  # Nhảy lên

        # Cập nhật vị trí của Dino sau mỗi khung hình (ví dụ: sử dụng vận tốc)
        dino.y += 5  # Mô phỏng vận tốc rơi tự do (có thể điều chỉnh)

        # Kiểm tra va chạm giữa Dino và các đối tượng
        if check_collision(dino, objects):
            print("Game Over!")  # Xử lý khi va chạm xảy ra

        # Vẽ Dino và các đối tượng lên khung hình (chỉ minh họa, bạn cần sử dụng OpenCV)
        frame = np.zeros((400, 400, 3), dtype=np.uint8)
        cv2.rectangle(frame, (dino.x, dino.y), (dino.x + dino.width, dino.y + dino.height), (0, 255, 0), -1)
        for obj in objects:
            cv2.rectangle(frame, (obj.x, obj.y), (obj.x + obj.width, obj.y + obj.height), (255, 0, 0), -1)

        cv2.imshow("Game", frame)

        # Thoát khỏi vòng lặp khi ấn phím ESC
        if key == 27:
            break

    cv2.destroyAllWindows()
