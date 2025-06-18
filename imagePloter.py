import cv2

# クリック時に座標を表示する関数
def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: ({x}, {y})")

# 画像を読み込む
image = cv2.imread('24837437_l.jpg')

window_width, window_height = 800, 600
height, width = image.shape[:2]
aspect_ratio = width / height


if aspect_ratio > window_width / window_height:
  new_width = window_width
  new_height = int(window_width / aspect_ratio)
else:
  new_height = window_height
  new_width = int(window_height * aspect_ratio)

resized_image = cv2.resize(image, (new_width, new_height))


# 画像を表示する
cv2.imshow('Image', resized_image)

# マウスクリックイベントを登録
cv2.setMouseCallback('Image', show_coordinates)

# キー入力待ち
cv2.waitKey(0)
cv2.destroyAllWindows()
