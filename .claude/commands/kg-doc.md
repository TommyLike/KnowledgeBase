# /kg-doc <pdf-path> [--out <dir>]

用 docling 将 PDF 转为结构化 Markdown + 提取图片和表格。

## 读取范围

本命令只操作 PDF 文件。允许读：
- 用户指定的 PDF 文件

禁止读：
- projects/ 任何文件
- references/ 任何文件
- config/ 任何文件

允许写：
- 输出目录 (index.md + images/)

## 行为

1. 调用 `scripts/docling-convert.py <pdf-path> [output-dir]`
2. 默认输出到 PDF 同目录下的 `<pdf-name>-docling/`
3. 输出包含：
   - `index.md` — 结构化 Markdown (含层级标题、表格、图片引用)
   - `images/page_XXX.png` — 逐页高清截图 (2x 缩放)
   - `images/pic_XXX.png` — PDF 内嵌图片
4. macOS 自动启用 MPS GPU 加速

## 依赖

- uvx (`pip install uv`)
- docling (`uvx --from docling-mcp[local]` 自动安装)
- PyTorch (docling 自动安装)

## 使用示例

```
/kg-doc products/ascend/950/白皮书.pdf
/kg-doc ~/Downloads/paper.pdf --out reports/papers/paper-docling
```
