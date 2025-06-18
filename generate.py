import torch
from transformers import AutoModel, AutoProcessor
from PIL import Image


# モデルID
model_id = "turing-motors/Heron-NVILA-Lite-2B"

# モデルとプロセッサのロード
model = AutoModel.from_pretrained(
    model_id,
    trust_remote_code=True,
    torch_dtype=torch.float16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained(model_id, trust_remote_code=True)

# 入力画像とテキスト
#webから
# image_url = "http://images.cocodataset.org/val2017/000000039769.jpg"
# image = Image.open(requests.get(image_url, stream=True).raw).convert("RGB")
#ローカルから
image_path = "24837437_l.jpg"
image = Image.open(image_path).convert("RGB")

text = "この画像のウサギの種類は何ですか。"

# 推論
response = model.generate_content([image, text])
print("出力:", response)
