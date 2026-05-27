# bank-proof-demo

> 截图OCR + 银行流水PDF自动标红框 — 演示版

## 这是什么

把微信/支付宝截图和官方流水PDF做匹配，自动在PDF上框出对应交易行。

**这是演示版**，展示核心能力。完整版含GUI、自动匹配引擎、多银行适配、AI纠错、批量处理等，不在此仓库中。

## 快速体验

```bash
pip install PyMuPDF pdfplumber openpyxl
python pipeline/demo_pipeline.py
```

## 项目结构

```
bank-proof-demo/
├── core/
│   ├── ocr.py              # OCR数据处理（演示用）
│   ├── pdf_highlight.py    # PDF表格提取 + 红色整行外框
│   └── export.py           # 标注后PDF导出
├── pipeline/
│   └── demo_pipeline.py    # 演示流程
├── demo/
│   └── sample_data.json    # 演示OCR数据
├── screenshots/            # 效果截图
├── LICENSE                 # CC BY-NC-ND 4.0
├── README.md
└── requirements.txt
```

## 核心能力

| 模块 | 说明 |
|------|------|
| PDF表格解析 | pdfplumber 提取交易行坐标 |
| 红色整行标注 | PyMuPDF 整行外框，不改内容和排版 |
| 关键词过滤 | 只框出含指定词的交易行 |
| OCR加载 | 从JSON加载已有的识别结果 |

## 技术栈

Python + pdfplumber + PyMuPDF + 智谱 GLM-4V-Flash

## License

CC BY-NC-ND 4.0 — 可查看学习，不可商用，不可修改分发。

## 关于完整版

本仓库仅演示核心技术方案。如需完整功能请通过 Issues 联系。
