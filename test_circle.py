import cv2
import torch
from transformers import AutoModel, AutoProcessor
from PIL import Image

# ==== Step 1: モデルの準備 ====
model_id = "turing-motors/Heron-NVILA-Lite-2B"
model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype=torch.float16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

# ==== Step 2: 入力画像の読み込み ====
image_path = "alphabet.png"
# image_path = "24837437_l.jpg"
original_cv_img = cv2.imread(image_path)
image_cv = original_cv_img.copy()  # 描画用コピー

selected_coords = []

# ==== Step 3: マウスクリックで座標取得 & 丸描画 ====
def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        selected_coords.clear()
        selected_coords.extend([x, y])
        print(f"選択された座標: ({x}, {y})")
        
        # 丸を描画（青色・太さ2）
        annotated = image_cv.copy()
        cv2.circle(annotated, (x, y), radius=30, color=(255, 0, 0), thickness=3)
        cv2.imshow("Image", annotated)
        cv2.imwrite("annotated_image.jpg", annotated)

# ==== Step 4: 画像表示とマウスイベント登録 ====
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
cv2.imshow("Image", image_cv)
cv2.setMouseCallback("Image", on_mouse_click)

print("画像をクリックして注目領域を選んでください。何かキーを押すと処理を続行します。")
cv2.waitKey(0)
cv2.destroyAllWindows()

# ==== Step 5: モデル推論 ====
if selected_coords:
    # 丸が描かれた画像をPILとして読み込み
    annotated_pil = Image.open("annotated_image.jpg").convert("RGB")

    # プロンプトに座標を含める（オプション）
    x, y = selected_coords
    prompt = f"この画像の丸で囲まれた部分には何がありますか？"
    print(f"プロンプト: {prompt}")

    # 推論
    response = model.generate_content([annotated_pil, prompt])
    print("出力:", response)

else:
    print("座標が選択されていません。もう一度実行してください。")
