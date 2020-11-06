# Python 中的 HTML 转 PDF 工具简单测试示例

测试的 Python 包：

- weasyprint
- pdfkit

测试总结：

- 在 Windows 下，使用 pdfkit 包比 weasyprint 包比较繁琐，需要下载 wkhtmltopdf 工具并添加环境变量，weasyprint 只需要安装 GTK+ 即可；
- pdfkit 转换 HTML 出现样式丢失的问题，weasyprint 没有该问题。
