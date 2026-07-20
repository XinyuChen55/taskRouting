"""
内网 OCR 服务封装。
传图 + askContent 进去, 服务端用多模态模型读图并按 askContent 提示返回 100 字描述。
"""

import os
import requests


OCR_URL = "https://llmservice.phfund.com.cn/multi-ocr2/ocr/upload"
OCR_TOKEN = "6f7c18535fc822bde129d6aa125b4678"


def upload_image_and_get_analysis(
    img_path: str,
    ask_content: str,
    project_name: str = "AI画像",
) -> str | None:
    """
    传图 + 提示词, 返回服务端模型的描述文本; 失败返回 None。

    Parameters
    ----------
    img_path : str
        本地图片路径 (.png/.jpg)
    ask_content : str
        提示词, 告诉模型怎么看这张图 (例: "请用 100 字分析此基金股票仓位走势曲线...")
    project_name : str
        分类标签, 默认 "AI画像"
    """
    if not os.path.exists(img_path):
        print(f"OCR error: file {img_path} not found")
        return None

    with open(img_path, "rb") as f:
        files = {
            "file": (os.path.basename(img_path), f, "image/png"),
            "projectName": (None, project_name),
            "askContent": (None, ask_content),
        }
        headers = {"Authorization": f"Bearer {OCR_TOKEN}"}
        try:
            resp = requests.post(OCR_URL, files=files, headers=headers, timeout=60)
            resp.raise_for_status()
            result = resp.json()
            if result.get("code") == 0:
                return result["msg"]["choices"][0]["message"]["content"]
            print(f"OCR API error code: {result.get('code')}")
            return None
        except Exception as e:
            print(f"OCR request failed: {e}")
            return None
