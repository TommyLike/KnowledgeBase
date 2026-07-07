#!/usr/bin/env -S uvx --from "docling-mcp[local]" python3
"""docling PDF 转换脚本 — PDF → Markdown + 图片 + 表格

用法:
  scripts/docling-convert.py <pdf-path> [output-dir]

环境变量:
  DOCLING_DEVICE=mps        macOS Apple Silicon GPU 加速 (默认)
  DOCLING_DEVICE=cpu        强制 CPU

输出:
  <output-dir>/
    index.md                结构化 Markdown (含表格、层级标题、图片引用)
    images/page_XXX.png     逐页截图 (高清, 2x 缩放)
    images/pic_XXX.png      内嵌图片

依赖: uvx (pip install uv)
"""
import os, sys, time

# --- MPS 加速 (macOS Apple Silicon) ---
if "DOCLING_DEVICE" not in os.environ:
    os.environ["DOCLING_DEVICE"] = "mps"

from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableStructureOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

def convert(pdf_path: str, out_dir: str):
    os.makedirs(f"{out_dir}/images", exist_ok=True)
    pdf_path = os.path.abspath(pdf_path)

    import torch
    device = os.environ.get("DOCLING_DEVICE", "cpu")
    mps_ok = torch.backends.mps.is_available() if device == "mps" else False
    print(f"🚀 docling | PyTorch {torch.__version__} | {device.upper()}{' ✅' if mps_ok else ' (fallback CPU)'}")

    accel = AcceleratorOptions(
        num_threads=8,
        device=AcceleratorDevice.MPS if mps_ok else AcceleratorDevice.CPU
    )
    pipeline = PdfPipelineOptions()
    pipeline.accelerator_options = accel
    pipeline.do_ocr = True
    pipeline.do_table_structure = True
    pipeline.table_structure_options = TableStructureOptions(do_cell_matching=True)
    pipeline.generate_page_images = True
    pipeline.generate_picture_images = True
    pipeline.images_scale = 2.0

    converter = DocumentConverter(format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline)
    })

    print(f"📄 {pdf_path}")
    t0 = time.time()
    result = converter.convert(pdf_path)
    elapsed = time.time() - t0

    doc = result.document
    page_count = len(result.pages)
    print(f"⏱️  {elapsed:.1f}s | 文本:{len(doc.texts)} 表格:{len(doc.tables)} 图片:{len(doc.pictures)} 页:{page_count}")

    # --- 提取页面图片 ---
    saved = 0
    for pi, page in enumerate(result.pages):
        try:
            img = page.get_image()
            if img and hasattr(img, 'size') and img.size[0] > 0:
                img.save(f"{out_dir}/images/page_{pi:03d}.png")
                saved += 1
        except: pass

    # --- 提取内嵌图片 ---
    for i, pic in enumerate(doc.pictures):
        try:
            img = pic.get_image(doc)
            if img and hasattr(img, 'size') and img.size[0] > 0:
                img.save(f"{out_dir}/images/pic_{i:03d}.png")
                saved += 1
        except: pass

    # --- 替换占位符 → Markdown 图片引用 ---
    md = doc.export_to_markdown()
    img_idx = 0
    lines = []
    for line in md.split('\n'):
        if line.strip() == '<!-- image -->':
            fname = f"page_{img_idx:03d}.png"
            exists = os.path.exists(f"{out_dir}/images/{fname}")
            lines.append(f'![图{img_idx+1}](images/{fname if exists else "missing.png"})')
            img_idx += 1
        else:
            lines.append(line)

    md_path = os.path.join(out_dir, "index.md")
    with open(md_path, "w") as f:
        f.write('\n'.join(lines))

    print(f"✅ 图片: {saved} 张 | MD: {len(md)} 字符/{md.count(chr(10))} 行")
    print(f"✅ 输出: {out_dir}/")
    return out_dir

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: docling-convert.py <pdf-path> [output-dir]")
        print("示例: docling-convert.py paper.pdf ./output")
        sys.exit(1)

    pdf = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else pdf.replace('.pdf', '-docling')
    if not os.path.exists(pdf):
        print(f"❌ 文件不存在: {pdf}")
        sys.exit(1)

    convert(pdf, out)
