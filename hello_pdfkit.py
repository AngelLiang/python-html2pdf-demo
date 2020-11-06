"""
    pip install pdfkit

使用 pdfkit 需要安装 wkhtmltopdf

    Windows下载地址： https://wkhtmltopdf.org/downloads.html

    Windows安装后还需要设置环境变量

        PATH="D:\Program Files\wkhtmltopdf\bin"


    Debian/Ubuntu 安装方式

        sudo apt-get install wkhtmltopdf


发现的bug：无法加载 css 文件

https://github.com/JazzCore/python-pdfkit/
"""
import pdfkit

options = {
    'encoding': 'UTF-8'
}
pdfkit.from_file('./order.html', 'hello_pdfkit.pdf',
                 options=options, css='pdf.css')
