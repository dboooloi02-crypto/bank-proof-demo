"""
PDF导出 — 标注后文件复制到输出目录
"""
import os
import shutil


def export_pdf(src_path: str, output_dir: str, pdf_name: str,
               suffix: str = "\u6807\u6ce8") -> str:
    os.makedirs(output_dir, exist_ok=True)
    out_name = f"{suffix}_{pdf_name}"
    out_path = os.path.join(output_dir, out_name)
    if src_path != out_path:
        shutil.move(src_path, out_path)
    print(f"[导出] {out_path}")
    return out_path
