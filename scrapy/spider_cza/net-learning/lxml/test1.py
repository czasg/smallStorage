from lxml.html import open_in_browser, etree

"""
from lxml.html import open_in_browser, etree

open_in_browser: 可以将对应的html使用浏览器打开
etree.tostring(html): 将html转化为string
etree.fromstring(string): 将string转化为html
"""

s = """<table><tr><td>11</td><td>2</td></tr><tr><td>3</td><td>4</td></tr></table>"""
open_in_browser(etree.fromstring(s), encoding="utf-8")
