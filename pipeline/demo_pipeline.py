"""
演示流水线 — 展示核心流程，使用demo数据
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from core.pdf_highlight import PdfHighlighter
from core.export import export_pdf

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    demo_dir = os.path.join(script_dir, "..", "demo")
    demo_pdf = os.path.join(demo_dir, "sample_bank.pdf")

    if not os.path.exists(demo_pdf):
        print(f"[错误] 未找到演示PDF: {demo_pdf}")
        print("[提示] 请将银行流水PDF放入 demo/ 目录并重命名为 sample_bank.pdf")
        return

    print("=" * 50)
    print("  bank-proof-demo")
    print("  银行流水PDF \u2192 \u7ea2\u8272\u6574\u884c\u5916\u6846")
    print("=" * 50)

    hl = PdfHighlighter()
    rows = hl.get_table_rows(demo_pdf)
    if not rows:
        return
    print(f"  \u2705 \u63d0\u53d6\u5230 {len(rows)} \u884c")

    keyword = "\u8f6c\u8d26"
    print(f"\n[2/4] \u5173\u952e\u8bcd\u8fc7\u6ee4..." + keyword)
    matched = [r for r in rows if keyword in r["row_text"]]
    if not matched:
        matched = [rows[0]]
    print(f"  {len(matched)} \u884c")

    hl_path = hl.highlight(demo_pdf, matched)
    output_dir = os.path.join(script_dir, "..", "output")
    out = export_pdf(hl_path, output_dir, os.path.basename(demo_pdf))

    print(f"\n  \u2705 {len(matched)} \u884c\u5df2\u6807\u6ce8 \u2192 {out}")

if __name__ == "__main__":
    main()
