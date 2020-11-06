"""
    pip install weasyprint

Windows 使用 weasyprint 还需要安装 GTK+：

    https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer

"""
import weasyprint

weasyprint.HTML(filename='order.html').write_pdf(
    'hello_weasyprint.pdf', stylesheets=[
        weasyprint.CSS('pdf.css')
    ])
