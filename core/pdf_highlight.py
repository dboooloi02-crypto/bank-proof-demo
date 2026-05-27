"""
PDF标注 — 红色整行外框
pdfplumber提取表格行 → PyMuPDF画annotation
"""
import os
import tempfile
import pdfplumber
import fitz


class PdfHighlighter:
    """PDF标注器"""

    def __init__(self, color=(1, 0, 0), border_width=3):
        self.color = color
        self.border_width = border_width

    def get_table_rows(self, pdf_path: str) -> list:
        rows = []
        with pdfplumber.open(pdf_path) as doc:
            for page_num in range(len(doc.pages)):
                page = doc.pages[page_num]
                for table in page.find_tables():
                    for ri, row in enumerate(table.rows):
                        if row.bbox is None:
                            continue
                        texts = []
                        for cell in row.cells:
                            try:
                                txt = page.within_bbox(cell).extract_text() or ""
                            except:
                                txt = ""
                            texts.append(txt.strip())
                        row_text = " ".join(texts)
                        if row_text.strip():
                            rows.append({
                                "page": page_num,
                                "row_bbox": row.bbox,
                                "row_text": row_text,
                                "row_idx": ri,
                            })
        print(f"[PDF] 提取 {len(rows)} 行表格数据")
        return rows

    def highlight(self, pdf_path: str, matched_rows: list) -> str:
        if not matched_rows:
            return pdf_path
        doc = fitz.open(pdf_path)
        for pg in doc:
            for a in list(pg.annots()):
                pg.delete_annot(a)
        seen = set()
        for mr in matched_rows:
            pn = mr["page"]
            rk = (pn, mr.get("row_idx", 0))
            if rk in seen:
                continue
            seen.add(rk)
            rb = mr["row_bbox"]
            rect = fitz.Rect(rb[0] - 1, rb[1] - 1, rb[2] + 1, rb[3] + 1)
            a = doc[pn].add_rect_annot(rect)
            a.set_colors(stroke=self.color)
            a.set_border(width=self.border_width)
            a.update()
        tmp = tempfile.NamedTemporaryFile(
            delete=False, suffix=".pdf", dir=os.path.dirname(pdf_path)
        )
        out = tmp.name
        tmp.close()
        doc.save(out, garbage=4, deflate=True)
        doc.close()
        print(f"[PDF] 标注完成: {len(seen)} 行")
        return out
