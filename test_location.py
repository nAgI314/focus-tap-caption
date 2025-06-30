import cv2
import torch
from transformers import AutoModel, AutoProcessor
from PIL import Image

print("実行")
model_id = "turing-motors/Heron-NVILA-Lite-2B"
model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype=torch.float16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

# image_path = "24837437_l.jpg"
image_path = "alphabet.png"
image_pil = Image.open(image_path).convert("RGB")
image_cv = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)  # OpenCV用
selected_coords = []

def show_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_coords.clear()
        selected_coords.extend([x, y])
        print(f"選択された座標: ({x}, {y})")
        cv2.circle(image_cv, (x, y), 5, (255, 0, 0), -1)
        cv2.imshow('Image', image_cv)

cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.imshow('Image', image_cv)
cv2.setMouseCallback('Image', show_coordinates)

print("画像をクリックして、説明したい場所を選んでください。何かキーを押すと処理を続行します。")
cv2.waitKey(0)
cv2.destroyAllWindows()

if selected_coords:
    x, y = selected_coords
    prompt = f"左上の座標を(0,0)右下の座標を(320,226)として、この画像の座標({x}, {y})付近に写っているものは何ですか？"
    print(f"プロンプト: {prompt}")

    response = model.generate_content([image_pil, prompt])
    print("出力:", response)

else:
    print("座標が選択されていません。もう一度実行してください。")
