"""
OCR数据处理 — 演示版
仅加载已有的JSON识别结果，不包含真实OCR调用
"""
import json
import os


class OCRItem:
    """单条OCR结果"""
    def __init__(self, data: dict):
        self.source = data.get("source", "")
        self.time = data.get("time", "")
        self.amount = data.get("amount", "")
        self.type = data.get("type", "")
        self.counterparty = data.get("counterparty", "")
        self.trade_no = data.get("trade_no", "")
        self.platform = data.get("platform", "")

    def __repr__(self):
        return f"[{self.platform}] {self.amount} | {self.counterparty}"


def load_ocr_data(path: str) -> list:
    """从JSON文件加载OCR识别结果"""
    if not os.path.exists(path):
        print(f"[OCR] 数据文件不存在: {path}")
        return []
    with open(path, encoding="utf-8") as f:
        raw = json.load(f)
    items = [OCRItem(r) for r in raw]
    print(f"[OCR] 加载 {len(items)} 条数据")
    return items
